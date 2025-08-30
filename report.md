📑 Project Report

Project Title: SanskritiAI – Indian Festival Archive

**Team Information**

| Name                            | Role                                   | Responsibilities                                                                  |
| ------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------- |
| **Karthik Balaji Sirimilla**    | Project Lead / Product Manager         | Define project scope & features, manage sprint goals, coordinate team progress    |
| **Prabhankith**                 | Full-Stack Developer                   | Build Streamlit UI, integrate SQLite database, develop festival submission forms  |
| **Pooja Nalajala**              | AI Engineer                            | Implement AI translation using Deep Translator, ensure multilingual accuracy      |
| **Agulla Prasanna**             | UI/UX Designer & Engagement Strategist | Design user-friendly layouts, apply Streamlit themes, add icons & navigation      |
| **Varshitha Sri Sai Nallapudi** | QA & Testing Lead                      | Test app on multiple devices/browsers, report bugs, validate file upload/deletion |


**1. Introduction**

India is a land of diverse cultures, languages, and traditions. Festivals are a significant aspect of its heritage, representing unity in diversity. However, there is no centralized digital repository that documents these festivals in an accessible and interactive way.

This project, SanskritiAI, is a Streamlit-based web application that aims to digitally preserve and present Indian festivals. It allows users to:

Submit festival details with descriptions and media.

Explore festivals through a chronological calendar.

Search festivals by keywords.

Translate festival descriptions into multiple Indian languages using AI.

**2. Objectives**

To design a corpus collection engine for Indian festivals.

To provide multilingual support for accessibility.

To enable supervised content management (upload + delete functionality).

To create a user-friendly Streamlit web interface for browsing and searching cultural data.

**3. Methodology**

**3.1 Tools & Frameworks**

Frontend & App Framework: Streamlit

Database: SQLite

AI Translation: Deep Translator (Google Translate backend)

Programming Language: Python

**3.2 System Workflow**

Data Collection: Users can submit new festival entries (name, region, date, description, media).

Data Storage: Entries are stored in SQLite database with optional images/videos.

Search & Retrieval: Full-text search (FTS5) allows retrieval by keywords.

Translation: Festival descriptions are translated into multiple Indian languages using AI.

Supervisor Controls: Admins can delete uploaded media if necessary.

**4. Implementation**

**4.1 Key Features**

Home Page: Overview and instructions.

Submit Festival: Form to add festivals with optional media (image/video).

Festival Calendar: Chronological list of festivals with translations and media previews.

Search Festivals: Keyword search using SQLite FTS5.

AI-Powered Translation: Descriptions can be instantly translated into Hindi, Tamil, Telugu, Bengali (extendable).

Supervisor Media Deletion: Admins can remove uploaded files if inappropriate.
**4.2 Sample Preloaded Festivals**

| Festival | Region      | Date        | Description                            |
| -------- | ----------- | ----------- | -------------------------------------- |
| Diwali   | Pan India   | 20-Oct-2025 | Festival of Lights.                    |
| Pongal   | Tamil Nadu  | 15-Jan-2025 | Harvest festival dedicated to Sun God. |
| Bihu     | Assam       | 14-Apr-2025 | Assamese New Year & harvest festival.  |
| Holi     | North India | 14-Mar-2025 | Festival of colors & spring.           |

**5. AI Integration**

The AI component of this project is the automatic multilingual translation of festival descriptions.

Library Used: deep-translator

Languages Supported: Hindi, Tamil, Telugu, Bengali (extendable)

Why AI? This ensures accessibility for people across India who may prefer different languages, making the archive inclusive.

Fallback: If translation fails, the app shows an error message gracefully without breaking.

**6. Results**

Successfully built an AI-powered cultural archive.

Users can submit, browse, and search festivals seamlessly.

Descriptions can be translated into Indian languages instantly.

Application supports supervised deletion of uploaded media.

Data is stored locally in SQLite with easy retrieval.

**7. Conclusion**

This project demonstrates how technology and AI can preserve India’s cultural diversity. By creating a centralized, multilingual, and searchable archive of festivals, SanskritiAI provides a scalable solution for documenting intangible heritage.

The project meets the internship requirements by:

Designing a corpus collection engine.

Adding AI functionality (translation).

Providing a clean, professional codebase with Streamlit.

**8. Future Scope**

Expand to support all Indian languages.

Add festival clustering & recommendation using embeddings.

Deploy the app on Streamlit Cloud / Hugging Face Spaces for wider access.

Enable crowdsourced moderation for verifying festival data.
