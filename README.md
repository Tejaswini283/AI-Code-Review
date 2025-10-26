
---

````markdown
# 🤖 AI Code Review Assistant

A Streamlit web app that uses OpenAI’s GPT model to review code, identify potential issues, and suggest improvements — all in real time.  
Try it live here 👉 [AI Code Review App](https://ai-code-review-dutiaqljkwjpxdwalxjafo.streamlit.app/)

---

## 🚀 Overview

The **AI Code Reviewer** lets you paste your code directly into a web interface and receive instant, AI-generated feedback.  
It’s useful for:
- Quick syntax and structure reviews  
- Learning better code practices  
- Improving code readability and maintainability  

The app supports multiple languages including **Python, SQL, JavaScript, and more**.

---

## Features

Instant code review powered by **OpenAI GPT-4o-mini**  
Simple, responsive **Streamlit UI**  
 Error handling for quota and API issues  
Secure API key management via **Streamlit Secrets**  

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** OpenAI API  
- **Language:** Python 3.9+  

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<your-username>/AI-Code-Review.git
cd AI-Code-Review
````

### 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your OpenAI API key

Create a folder `.streamlit` and add a file named `secrets.toml`:

```toml
OPENAI_API_KEY="sk-your_api_key_here"
```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

Then open the URL Streamlit shows (usually [http://localhost:8501](http://localhost:8501)).

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your project to GitHub
2. Go to [https://share.streamlit.io/](https://share.streamlit.io/)
3. Connect your repo and deploy
4. Add your API key under **App → Settings → Secrets**:

   ```toml
   OPENAI_API_KEY="sk-your_api_key_here"
   ```

---

## 🧾 Example Prompt

Paste code like this:

```sql
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;
```

And get feedback such as:

> “Consider using explicit JOIN syntax instead of implicit joins for clarity.
> Add indexes on `City` if this query runs frequently.”

---

## 🧰 File Structure

```
AI-Code-Review/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Project dependencies
├── .gitignore            # Files to ignore (e.g., secrets.toml)
└── .streamlit/
     └── secrets.toml     # Your private API key (not uploaded)
```

---

## 🛡️ Notes

* Do **NOT** upload your `secrets.toml` file to GitHub.
* If you get a “RateLimitError” or “Quota exceeded,” check your [OpenAI usage dashboard](https://platform.openai.com/account/usage).

---

## 💡 Future Enhancements

* Support for file upload (.py, .sql, .js)
* Syntax highlighting in feedback
* Multiple model options (GPT-4o, GPT-4-turbo)
* Option to auto-fix common issues

---
