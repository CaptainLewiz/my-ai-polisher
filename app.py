import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🚀 My AI Polisher")

user_input = st.text_area("Paste messy text here:")

if st.button("Fix It ✨"):
if user_input:
chat = client.chat.completions.create(
messages=[{"role": "user", "content": f"Make this professional: {user_input}"}],
model="llama-3.3-70b-versatile",
)
st.success(chat.choices[0].message.content)
