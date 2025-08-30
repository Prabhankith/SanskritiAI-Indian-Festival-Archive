📄 INDIAN FESTIVALS: Culture Collector – Preserving Heritage Through AI
1.1 Team Information
Name	Role	Responsibilities
Saketh	Project Lead / Product Manager	Define app features, manage sprint goals, coordinate team progress
Sony	Full-Stack Developer	Build Streamlit UI, integrate SQLite storage, create submission forms
Adil	AI Engineer	Implement translation module (MarianMT), test multilingual outputs
Divya	UI/UX Designer & Engagement Strategist	Design user-friendly layouts, add themes, icons, improve navigation
Himashu	QA & Testing Lead	Cross-device/browser testing, handle bug tracking, check safe deletion of files
1.2 Application Overview – MVP Scope

Project Name: INDIAN FESTIVALS – Culture Collector

Problem Statement: India is home to thousands of festivals across regions, religions, and communities. Much of this cultural heritage remains undocumented, scattered, or at risk of being lost in oral and local traditions. Current AI systems also lack exposure to culturally rich text describing these festivals. This project aims to crowdsource festival knowledge, storing it in structured form while enabling translation into multiple languages for accessibility.

MVP Objective
Build a Streamlit Web App where users can:

Submit festival details (name, date, description, region, image).

View festivals on a calendar and in a searchable database.

Translate festival descriptions into English or other languages.

Safely handle missing/deleted images without breaking UI.

Optimize for offline-first usage (local storage with SQLite).

1.3 AI Integration Details

AI Modules in MVP:

Translation – Festival descriptions can be translated into English (or other languages) using Hugging Face MarianMT models.

Future Scope:

Text-to-Speech (TTS) for hearing festival descriptions in native language.

Semantic search (search by meaning, not exact keyword).

Automatic tagging (religion, region, type of festival).

All AI features are implemented with open-source libraries for transparency and offline-friendly design.

1.4 Technical Architecture & Development

Tech Stack

Frontend: Streamlit (Python)

Backend: SQLite (local database storage)

AI Processing: Hugging Face Transformers (MarianMT for translation)

Deployment: Streamlit Cloud / Hugging Face Spaces

Database

Stored in data/festivals.db

Contains tables for festival details and metadata

Images stored in images/ folder with safe checks

Development Breakdown

Day	Focus	Deliverables
1	App structure & UI	Streamlit pages (Home, Submit, Calendar, Search)
2	Database logic	SQLite schema + CRUD operations
3	AI Integration	Translation of festival descriptions
4	Calendar & Search	Calendar display + keyword search
5	File Safety	Graceful handling of deleted images
6	Testing & polish	Cross-device checks, bug fixes
7	Deployment	Push to Hugging Face / Streamlit Cloud
1.5 User Testing & Feedback (Week 2)

Methodology
Tested with:

Students and community members interested in culture

Rural users with low bandwidth connections

Different devices (mobiles, laptops, browsers)

Testing Tasks

Submit new festivals (with and without images)

Translate descriptions

Use calendar navigation and search

Check deleted/missing image behavior

Feedback Loop

Feedback Theme	Insights Collected	Actions Taken
Missing image errors	App crashed if image was deleted	Added safe check to skip images
Translation clarity	Some outputs too literal	Added “optional edit after translation”
Calendar UX	Users wanted hover details	Improved tooltips and descriptions
Mobile experience	Long text wrapping poorly	Adjusted CSS/styling for readability
1.6 Project Lifecycle & Roadmap
Week 1: MVP Build & Deployment

Objective: Working app with database + translation

Deliverables: Submission form, calendar, search, AI translation

Week 2: Beta Testing & Iterations

Objective: Collect real user feedback

Methodology: Tested under low bandwidth, mobile-first conditions

Expected Outcomes: Improved UI, translation flow, safe file handling

Weeks 3–4: Scaling & Outreach Campaign

Target Audience: Schools, cultural clubs, WhatsApp groups, heritage communities

Execution:

Daily “Festival Fact” campaign on social media

Direct outreach to student groups for contributions

Metrics:

Target: 1000+ festival entries across 20+ states

Measure: Active users, number of contributions, language coverage

Post-Internship Vision & Sustainability

Future Features

Community “Festival of the Day” voting

AI clustering of festivals by region/religion

TTS + voice input for accessibility

Community Building

Encourage cultural groups and schools to contribute

Public leaderboard to recognize top contributors

Scaling

Extend to include rituals, foods, songs linked to festivals

Build an open corpus for AI cultural research

2. Code Repository Submission

Repository: [To be added]

Contents

app.py

requirements.txt

.gitignore

README.md

REPORT.md

data/festivals.db (sample dataset)

images/ (festival posters/photos)

3. Live Application Link

Deployment target: Hugging Face Spaces / Streamlit Cloud

4. Demo Video (5–7 mins)

A walkthrough covering:

Purpose of the app

Submitting festivals

AI-powered translation

Calendar & search features

Offline-first usage

🔒 End of Report
