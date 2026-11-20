
import streamlit as st
import pandas as pd
import json
from google import genai

# Page settings
st.set_page_config(
    page_title="AI Flashcard Generator",
    page_icon="📚",
    layout="wide"
)

# Gemini client
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Application heading
st.title("📚 AI Flashcard Generator")
st.write("Convert your study notes into question-and-answer flashcards using AI.")

st.divider()

# User input
notes = st.text_area(
    "Paste your study notes here:",
    height=250,
    placeholder="Paste your chapter notes, lecture notes or study material..."
)

number_of_cards = st.slider(
    "Number of flashcards",
    min_value=3,
    max_value=20,
    value=10
)

# Generate flashcards
if st.button("✨ Generate Flashcards", type="primary"):

    if not notes.strip():
        st.warning("Please paste your notes first.")

    else:
        prompt = f"""
        You are an educational flashcard generator.

        Create exactly {number_of_cards} useful revision flashcards
        using ONLY the study notes provided below.

        Return ONLY a valid JSON array.
        Each item must contain:
        - question
        - answer

        Do not include Markdown or explanations outside the JSON.

        Study notes:
        {notes}
        """

        try:
            with st.spinner("Generating your flashcards..."):

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                result = response.text.strip()

                # Remove Markdown code fences if returned
                if result.startswith("```"):
                    result = result.replace("```json", "")
                    result = result.replace("```", "").strip()

                flashcards = json.loads(result)

                if not isinstance(flashcards, list):
                    raise ValueError("AI did not return a JSON list.")

                # Validate the response
                clean_cards = []
                for card in flashcards:
                    if (
                        isinstance(card, dict)
                        and card.get("question")
                        and card.get("answer")
                    ):
                        clean_cards.append({
                            "Question": str(card["question"]),
                            "Answer": str(card["answer"])
                        })

                if not clean_cards:
                    raise ValueError("No valid flashcards were generated.")

                df = pd.DataFrame(clean_cards)

                st.session_state["flashcards"] = df

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# Display generated flashcards
if "flashcards" in st.session_state:

    df = st.session_state["flashcards"]

    st.success(f"{len(df)} flashcards generated successfully!")

    st.subheader("Your Flashcards")

    for index, row in df.iterrows():
        with st.expander(f"📝 Card {index + 1}: {row['Question']}"):
            st.write("**Answer:**")
            st.write(row["Answer"])

    st.divider()

    st.subheader("Download Flashcards")

    csv_data = df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="⬇️ Download Flashcards as CSV",
        data=csv_data,
        file_name="AI_Flashcards.csv",
        mime="text/csv"
    )
