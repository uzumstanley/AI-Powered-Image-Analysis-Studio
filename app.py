import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables and configure API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page configuration with custom theme
st.set_page_config(
    page_title="Gemini Vision Pro",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .uploadedImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    raise FileNotFoundError("No file uploaded")

# Sidebar with enhanced styling
with st.sidebar:
    st.title("🔮 Gemini Vision Pro")
    st.markdown("---")
    st.subheader("About")
    st.markdown("""
        Transform your images into insights with Gemini Vision Pro - powered by Google's 
        advanced gemini-2.0-flash-exp model for lightning-fast image analysis.
        
        **Features:**
        - Advanced OCR capabilities
        - Multi-format support
        - Real-time analysis
        - High accuracy results
    """)
    st.markdown("---")
    st.caption("Powered by Gemini AI 2.0")

# Main content area with two columns
col1, col2 = st.columns([3, 2])

with col1:
    st.title("📸 Image Analysis Studio")
    st.markdown("Upload your image and let Gemini AI reveal the insights within.")
    
    input_prompt = st.text_area(
        "What would you like to know about the image?",
        placeholder="E.g., Extract all text and analyze the content in detail...",
        height=100
    )
    
    uploaded_file = st.file_uploader(
        "Upload Image (JPEG/PNG)",
        type=["jpg", "jpeg", "png"],
        help="Drag and drop or click to upload"
    )

with col2:
    st.markdown("<br>" * 4, unsafe_allow_html=True)  # Add some spacing
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Preview", use_column_width=True, clamp=True)
    else:
        st.info("👆 Upload an image to get started")

# Analysis section
if st.button("🔍 Analyze with Gemini AI", key="analyze"):
    if not input_prompt.strip():
        st.error("⚠️ Please enter a query first")
    elif not uploaded_file:
        st.error("⚠️ Please upload an image to analyze")
    else:
        with st.spinner("🤖 Gemini AI is analyzing your image..."):
            try:
                image_data = input_image_setup(uploaded_file)
                detailed_prompt = """
                You are an advanced image analysis expert using the Gemini AI system.
                Analyze the provided image thoroughly and provide detailed insights
                based on the user's query. Include relevant details and maintain
                a professional tone in your response.
                """
                response = get_gemini_response(detailed_prompt, image_data, input_prompt)
                
                st.success("✨ Analysis Complete!")
                st.markdown("### 📊 Analysis Results")
                st.markdown(response)
                
                # Add option to download results
                st.download_button(
                    label="📥 Download Analysis",
                    data=response,
                    file_name="gemini_analysis.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"🚫 An error occurred: {str(e)}")
                st.info("💡 Tip: Try uploading a different image or refreshing the page")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Created with ❤️ using Streamlit and Gemini AI</p>
    </div>
    """,
    unsafe_allow_html=True
)