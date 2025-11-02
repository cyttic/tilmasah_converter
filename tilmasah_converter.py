import streamlit as st
import pandas as pd
import json
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

st.set_page_config(page_title="Word Preposition Manager", layout="centered")

st.title("📘 Word & Preposition Collector")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = []

# Input fields
col1, col2 = st.columns(2)
with col1:
    word = st.text_input("Word")
    preposition = st.text_input("Preposition")
with col2:
    example = st.text_input("Example")
    translate = st.text_input("Translate")

# Add button
if st.button("➕ Add"):
    if word and preposition and example and translate:
        st.session_state.data.append({
            "Word": word,
            "Preposition": preposition,
            "Example": example,
            "Translate": translate
        })
        st.success("✅ Added successfully!")
    else:
        st.warning("⚠️ Please fill in all fields!")

# Display table
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True)

    # Export to JSON
    json_data = json.dumps(st.session_state.data, ensure_ascii=False, indent=4)
    st.download_button(
        label="💾 Export to JSON",
        data=json_data.encode("utf-8"),
        file_name="words.json",
        mime="application/json"
    )

    # Export to PDF
    def create_pdf(data):
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        y = height - 50
        c.setFont("Helvetica", 12)
        c.drawString(50, y, "Word & Preposition List")
        y -= 30
        for row in data:
            line = f"{row['Word']} ({row['Preposition']}) - {row['Example']} [{row['Translate']}]"
            c.drawString(50, y, line)
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50
        c.save()
        buffer.seek(0)
        return buffer

    pdf_buffer = create_pdf(st.session_state.data)
    st.download_button(
        label="📄 Export to PDF",
        data=pdf_buffer,
        file_name="words.pdf",
        mime="application/pdf"
    )
else:
    st.info("No words added yet — start by filling the form above!")


