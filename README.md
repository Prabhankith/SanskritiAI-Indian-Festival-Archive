
# 🎉 Regional Festivals & Celebrations App

A community-driven Streamlit app that archives and shares Indian festivals, rituals, and cultural celebrations.

## 🚀 Features
- Submit festival info with images/videos
- Festival calendar view
- Search festivals with Full-Text Search
- Preloaded festivals (Diwali, Pongal, Bihu, Holi)

## 🛠️ Setup Instructions
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📂 Project Structure
```
festivals_app/
│── app.py
│── requirements.txt
│── README.md
│── festivals.db        # SQLite DB created automatically
│── uploads/            # Uploaded media stored here
```

## ✅ Preloaded Data
- Diwali (Pan India)
- Pongal (Tamil Nadu)
- Bihu (Assam)
- Holi (North India)
```
