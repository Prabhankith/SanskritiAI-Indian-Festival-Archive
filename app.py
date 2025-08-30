import streamlit as st
import sqlite3
import os
from datetime import datetime
from deep_translator import GoogleTranslator  # ✅ replaced transformers

DB_FILE = "festivals.db"
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

conn = sqlite3.connect(DB_FILE, check_same_thread=False)
c = conn.cursor()

# Tables
c.execute("""
CREATE TABLE IF NOT EXISTS festivals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    region TEXT,
    festival_date TEXT,
    description TEXT,
    media_path TEXT
)
""")
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS festivals_fts 
USING fts5(name, region, description, content='festivals', content_rowid='id')
""")
c.execute("""
CREATE TABLE IF NOT EXISTS translations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    festival_id INTEGER,
    lang TEXT,
    translated_text TEXT,
    UNIQUE(festival_id, lang)
)
""")
conn.commit()

# Translation languages (deep-translator codes)
LANG_CODES = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "Bengali": "bn"
}

def add_festival(name, region, date, description, media_path=""):
    c.execute("SELECT id FROM festivals WHERE name=? AND region=?", (name, region))
    if not c.fetchone():
        c.execute("INSERT INTO festivals (name, region, festival_date, description, media_path) VALUES (?, ?, ?, ?, ?)",
                  (name, region, date, description, media_path))
        last_id = c.lastrowid
        c.execute("INSERT INTO festivals_fts(rowid, name, region, description) VALUES (?, ?, ?, ?)",
                  (last_id, name, region, description))
        conn.commit()

def search_festivals(query):
    c.execute("SELECT rowid FROM festivals_fts WHERE festivals_fts MATCH ?", (query,))
    rows = c.fetchall()
    results = []
    for r in rows:
        c.execute("SELECT * FROM festivals WHERE id=?", (r[0],))
        results.append(c.fetchone())
    return results

def get_translation(festival_id, text, lang):
    """Retrieve or generate translation"""
    c.execute("SELECT translated_text FROM translations WHERE festival_id=? AND lang=?", (festival_id, lang))
    row = c.fetchone()
    if row:
        return row[0]
    
    if lang in LANG_CODES:
        try:
            translated = GoogleTranslator(source="en", target=LANG_CODES[lang]).translate(text)
            c.execute("INSERT OR IGNORE INTO translations(festival_id, lang, translated_text) VALUES (?, ?, ?)",
                      (festival_id, lang, translated))
            conn.commit()
            return translated
        except Exception as e:
            return f"(⚠️ Translation failed: {e})"
    else:
        return "(⚠️ No model available for this language)"

# Preload sample festivals
sample_festivals = [
    ("Diwali", "Pan India", "2025-10-20", "Festival of Lights, celebrating the victory of light over darkness."),
    ("Pongal", "Tamil Nadu", "2025-01-15", "Harvest festival dedicated to the Sun God."),
    ("Bihu", "Assam", "2025-04-14", "Assamese New Year festival, celebrating the harvest season."),
    ("Holi", "North India", "2025-03-14", "Festival of colors, symbolizing love and the arrival of spring."),
]
for fest in sample_festivals:
    add_festival(*fest)

# Streamlit UI
st.set_page_config(page_title="Indian Festivals Archive", layout="wide")
st.title("🎉 Regional Festivals & Celebrations of India")

menu = ["Home", "Submit Festival", "Festival Calendar", "Search Festivals"]
choice = st.sidebar.radio("Navigation", menu)

target_lang = st.sidebar.selectbox("🌐 Translate To", ["None"] + list(LANG_CODES.keys()))

if choice == "Home":
    st.header("Welcome to the Indian Festivals Archive 🇮🇳")
    st.write("""
        This app preserves India's rich cultural heritage.  
        - Submit new festivals with descriptions & media.  
        - Browse through the calendar of festivals.  
        - Search by name, region, or keywords.  
        - Translate festival descriptions into multiple Indian languages with AI.  
    """)

elif choice == "Submit Festival":
    st.subheader("📝 Submit a New Festival")
    with st.form("festival_form", clear_on_submit=True):
        name = st.text_input("Festival Name")
        region = st.text_input("Region")
        date = st.date_input("Festival Date", datetime.today())
        description = st.text_area("Description")
        media_file = st.file_uploader("Upload Image/Video", type=["jpg", "jpeg", "png", "mp4", "mov", "avi"])
        submitted = st.form_submit_button("Submit")

        if submitted:
            media_path = ""
            if media_file is not None:
                media_path = os.path.join(UPLOAD_DIR, media_file.name)
                with open(media_path, "wb") as f:
                    f.write(media_file.getbuffer())
            add_festival(name, region, str(date), description, media_path)
            st.success(f"✅ Festival '{name}' added successfully!")

elif choice == "Festival Calendar":
    st.subheader("📅 Festival Calendar")
    c.execute("SELECT * FROM festivals ORDER BY date(festival_date) ASC")
    festivals = c.fetchall()
    for fest in festivals:
        st.markdown(f"### {fest[1]} ({fest[2]}) - {fest[3]}")
        st.write(fest[4])
        if target_lang != "None":
            with st.expander(f"🌐 View in {target_lang}"):
                st.info(get_translation(fest[0], fest[4], target_lang))
        if fest[5] and os.path.exists(fest[5]):
            if fest[5].lower().endswith((".png", ".jpg", ".jpeg")):
                st.image(fest[5], caption=fest[1], use_container_width=True)
            elif fest[5].lower().endswith((".mp4", ".mov", ".avi")):
                st.video(fest[5])

elif choice == "Search Festivals":
    st.subheader("🔍 Search Festivals")
    query = st.text_input("Enter festival name, region, or keyword")
    if query:
        results = search_festivals(query)
        if results:
            for fest in results:
                st.markdown(f"### {fest[1]} ({fest[2]}) - {fest[3]}")
                st.write(fest[4])
                if target_lang != "None":
                    with st.expander(f"🌐 View in {target_lang}"):
                        st.info(get_translation(fest[0], fest[4], target_lang))
                if fest[5] and os.path.exists(fest[5]):
                    if fest[5].lower().endswith((".png", ".jpg", ".jpeg")):
                        st.image(fest[5], caption=fest[1], use_container_width=True)
                    elif fest[5].lower().endswith((".mp4", ".mov", ".avi")):
                        st.video(fest[5])
        else:
            st.info("No festivals found for your query.")
