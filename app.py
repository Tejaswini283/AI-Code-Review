import streamlit as st
from openai import OpenAI, RateLimitError, APIError  # ✅ Single correct import

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit page setup
st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🤖 AI Code Review Assistant")
st.write("Upload or paste your code, and the AI will provide suggestions for improvement.")

# Code input area
code_input = st.text_area("Paste your code here 👇", height=300)

# Button action
if st.button("Review Code"):
    if code_input.strip() == "":
        st.warning("Please paste some code first!")
    else:
        with st.spinner("Analyzing your code..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful code reviewer."},
                        {"role": "user", "content": f"Review the following code and provide constructive feedback:\n\n{code_input}"}
                    ]
                )
                review = response.choices[0].message.content
                st.subheader("🧾 Code Review")
                st.write(review)

            except RateLimitError:
                st.error("⚠️ You’ve exceeded your API quota. Please check your OpenAI billing settings.")
            except APIError as e:
                st.error(f"An error occurred: {e}")
