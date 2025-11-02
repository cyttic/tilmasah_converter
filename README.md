# 📘 Word & Preposition Collector

![App Screenshot](Screenshot.png)

A simple Streamlit web app for collecting words, prepositions, examples, and translations — designed to help language learners (especially for English ↔ Hebrew study).  
You can easily add new entries, view them in a table, and export your data to **JSON** or **PDF**.

---

## 🚀 Features

- 📝 Add new entries (Word, Preposition, Example, Translation)
- 📊 View all saved items in a clean table
- 💾 Export to **JSON**
- 📄 Export to **PDF** (supports Hebrew and other Unicode text)
- 🔤 Full UTF-8 compatibility — perfect for multilingual vocabulary

---

## 🧰 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/word-preposition-collector.git
   cd word-preposition-collector
   ```

2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install streamlit pandas reportlab python-bidi arabic-reshaper
   ```

4. (Optional) Download a Hebrew-capable font such as  
   [NotoSansHebrew-Regular.ttf](https://fonts.google.com/noto/specimen/Noto+Sans+Hebrew)  
   and place it in the same folder as the script.

---

## ▶️ Usage

Run the app:
```bash
streamlit run app.py
```

Then open the provided local URL (usually `http://localhost:8501`) in your browser.

---

## 📦 Exports

- **Export to JSON:** saves your data in a `.json` file using UTF-8 encoding.  
- **Export to PDF:** generates a clean PDF file with multilingual text support (English + Hebrew).

---

## 🧠 Example

Example Hebrew entry:

| Word | Preposition | Example | Translate |
|------|--------------|----------|------------|
| לטוס | על | הטייס הזה יודע לטוס על כל סוגי מטוס | This pilot can fly on any type of planes |

---

## 📜 License

This project is open-source under the **MIT License**.  
Feel free to use and modify it for your language-learning projects.

---

### 💡 Author

Created with ❤️ by [Your Name]
