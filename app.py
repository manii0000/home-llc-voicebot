
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

st.title("🎙️ Manisha's AI Interview Voicebot (Pro Version)")

# Define Manisha's profile for interview answers
system_prompt = """
You are Manisha's AI Interview Voice Agent. 
You will answer interview questions as if you are Manisha herself. 
Here is Manisha's information:
- Passionate about AI, NLP, LLMs, and intelligent agents.
- 1+ year experience in AI, ML, data science and NLP.
- Skilled in Python, Streamlit, LangChain, SQL, OpenAI, Google Gemini API, MySQL, Chroma, RAG pipeline.
- Built projects like Document QA bots, Economic Data Fetcher using API to SQL pipeline, Vehicle Number Plate Detection System, Sentiment Analysis using BERT.
- Has experience in chatbots, document question-answering, data analysis, and generative AI tools.
- Actively learning deep learning, computer vision, and building multi-agent systems.
- Loves solving complex problems and constantly improving skills.
Respond in first person, confidently, and warmly as Manisha would in an interview.
"""

# Input box for user to type interview question
question = st.text_input("💬 Ask your interview question:")

if st.button("Get Answer"):
    if question:
        # Generate answer using GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        st.write("🗣️ Answer:")
        st.write(answer)

        # Generate voice using OpenAI TTS
        audio_response = client.audio.speech.create(
            model="tts-1",  # Using tts-1 standard model
            voice="alloy",  # You can also try: "echo", "fable", "onyx", "nova", "shimmer"
            input=answer
        )

        # Save and play audio
        audio_file_path = "output.mp3"
        with open(audio_file_path, "wb") as f:
            f.write(audio_response.content)
        st.audio(audio_file_path)
    else:
        st.warning("Please enter your question.")
