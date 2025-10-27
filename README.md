
````markdown
# AI Code Review Assistant

This is an app that uses OpenAI’s API to review code.  
You can paste your code into the app, and it gives suggestions or feedback to help improve it.

Live app: [https://ai-code-review-dutiaqljkwjpxdwalxjafo.streamlit.app/]

---

## How it works

- The app is built with **Python** and **Streamlit**.  
- It sends your code to the **OpenAI API** using your API key.  
- The model reviews the code and returns suggestions or best-practice comments.  

---

## To run locally

1. Clone this repo:
   ```bash
   git clone https://github.com/<your-username>/AI-Code-Review.git
   cd AI-Code-Review
````

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key.
   Inside the project, create a folder called `.streamlit` and a file inside it named `secrets.toml`:

   ```toml
   OPENAI_API_KEY="sk-your_api_key_here"
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open the link shown in your terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## To deploy on Streamlit Cloud

1. Push this code to your GitHub repo.
2. Go to [https://share.streamlit.io](https://share.streamlit.io) and connect your repo.
3. In “Secrets”, add your API key as:

   ```toml
   OPENAI_API_KEY="sk-your_api_key_here"
   ```
4. Click “Deploy”.

---

## Notes

* Don’t upload your `secrets.toml` file to GitHub.
* If you see a “Rate limit” or “Quota exceeded” error, check your OpenAI usage page.
* Works best with Python 3.9 or higher.

---

## Example

You can paste something like:

```sql
SELECT A.CustomerName, B.CustomerName
FROM Customers A, Customers B
WHERE A.City = B.City;
```

The app will suggest improvements such as using proper JOIN syntax or indexing columns.
