# AI-Flashcard-Generator
An AI-powered Flashcard Generator that converts study notes into question-and-answer flashcards using an LLM. Generates structured JSON, processes data using Pandas DataFrame, displays interactive flashcards, and allows CSV export for quick revision.
# 📚 AI Flashcard Generator

An AI-powered Flashcard Generator that transforms lengthy study notes into concise question-and-answer flashcards for quick and effective revision.

## 🚀 Overview

The AI Flashcard Generator helps students simplify their learning process by automatically converting study notes into interactive flashcards using a Large Language Model (LLM).

Students can paste their notes, generate AI-powered questions and answers, review flashcards, and download them as a CSV file.

## ✨ Features

- 📝 **Paste Study Notes:** Enter or paste your study material.
- 🤖 **AI-Powered Generation:** Automatically generates relevant questions and answers using an LLM.
- 📋 **JSON Output:** Structures generated flashcards into JSON format.
- 📊 **Pandas Integration:** Loads and organizes flashcard data into a Pandas DataFrame.
- 🎴 **Interactive Flashcards:** View questions and reveal their answers.
- 📥 **CSV Export:** Download generated flashcards for offline use.
- ⚡ **Quick Revision:** Helps students revise important concepts efficiently.

## 🔄 Workflow

1. Paste study notes into the application.
2. Send notes to the LLM through the API.
3. Generate question-answer pairs in JSON format.
4. Parse the JSON response.
5. Convert the data into a Pandas DataFrame.
6. Display interactive flashcards.
7. Download flashcards as a CSV file.

## 🛠️ Technologies Used

- Python
- Large Language Model (LLM)
- Groq API
- Pandas
- JSON
- CSV

## 📂 Project Structure

```text
AI-Flashcard-Generator/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

*Note: Adjust the project structure according to your actual files.*

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd AI-Flashcard-Generator
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your API key**

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

**5. Run the application**

```bash
streamlit run app.py
```

*Use the run command appropriate to your actual application framework.*

## 🎯 Use Cases

- Students preparing for examinations.
- Quick revision of lecture notes.
- Learning technical concepts.
- Creating reusable study materials.
- Improving active recall and self-assessment.

## 🔮 Future Enhancements

- PDF and DOCX note uploads.
- Difficulty-based flashcard generation.
- Multiple-choice quiz generation.
- Flashcard history and saved decks.
- Spaced repetition for better learning.

## 👩‍💻 Author

**Vaishnavi Malwade**

AI Flashcard Generator – Making learning and revision easier with AI.

---

⭐ If you find this project useful, consider giving it a star!
