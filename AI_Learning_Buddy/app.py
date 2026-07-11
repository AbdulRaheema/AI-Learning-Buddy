import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Buddy")
st.write("Learn any topic with the help of Google Gemini AI.")

# Sidebar
st.sidebar.header("Settings")
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

topic = st.text_input("📘 Enter a Topic")

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

question = ""
if activity == "Ask Anything":
    question = st.text_area("Ask your question")

if st.button("Generate 🚀"):

    if client is None:
        st.error("Please enter your Gemini API Key.")
        st.stop()

    if activity != "Ask Anything" and topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    if activity == "Explain Concept":
        prompt = f"Explain {topic} in simple language for a beginner."

    elif activity == "Real-Life Example":
        prompt = f"Give one real-life example of {topic}."

    elif activity == "Generate Quiz":
        prompt = f"Create 5 multiple choice questions on {topic} with answers."

    else:
        prompt = question

    with st.spinner("Generating response..."):

        try:
            response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
            )

            st.success("Done!")

            st.markdown("## 📖 AI Response")
            st.write(response.text)

        except Exception as e:
            st.error(str(e))

st.markdown("---")
st.caption("Powered by Google Gemini • Built with Streamlit")
