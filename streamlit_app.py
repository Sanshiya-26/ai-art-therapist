import streamlit as st
from app.emotion import detect_emotion
from app.prompt_builder import build_prompt
from app.image_generator import generate_image

st.set_page_config(page_title="AI Art Therapist 🎨", layout="centered")

st.title("🎨 AI Art Therapist")
st.markdown("Describe how you're feeling. We'll turn it into art!")

text = st.text_area("What are you feeling right now?")
mode = st.selectbox("Choose a style:", ["reflect", "positive"])

if st.button("Generate Image"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing emotion and generating image..."):
            emotion, score = detect_emotion(text)
            prompt = build_prompt(emotion, mode)

            # ✅ Prompt validation
            if not prompt or len(prompt.strip()) < 5:
                st.error("Failed to build a valid image prompt. Please rephrase your input.")
            else:
                try:
                    image_path = generate_image(prompt)
                    st.success(f"Emotion Detected: **{emotion}** (Confidence: {score:.2f})")
                    st.image(image_path, caption=prompt)
                except Exception as e:
                    st.error("Image generation failed. Please try again with a different input.")
                    st.exception(e)  # Show error details for debugging

