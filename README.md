# Gemini Vision Pro - Image Analysis Studio

Gemini Vision Pro is an advanced image analysis tool powered by Google's Gemini AI 2.0. It allows users to upload images, input custom queries, and receive detailed insights based on the content of the image. With its advanced OCR capabilities and real-time processing, Gemini Vision Pro transforms any image into valuable information, providing users with an intuitive and powerful tool for image analysis.

## Features

- **Advanced OCR Capabilities**: Extract text from images with high accuracy.
- **Multi-format Support**: Supports JPEG, PNG, and other common image formats.
- **Real-time Analysis**: Instant results after uploading and inputting a query.
- **High Accuracy**: Powered by Gemini AI 2.0, ensuring precise and detailed analysis.

## Installation

To get started with Gemini Vision Pro, follow these steps:

### Prerequisites

1. **Python 3.8+**: Ensure you have Python 3.8 or later installed.
2. **Streamlit**: Gemini Vision Pro is built using Streamlit for a fast and interactive interface.
3. **dotenv**: Load environment variables securely for the API configuration.
4. **Pillow**: Used for image handling and previews.
5. **Google Generative AI**: Used for processing the image analysis and generating results.

### Step 1: Install Dependencies

To install the required dependencies, you can use pip:

```bash
pip install streamlit google-generativeai Pillow python-dotenv
```

### Step 2: Set Up API Key

- Obtain your API key for Google's Gemini AI from [Google Cloud](https://cloud.google.com).
- Create a `.env` file in the project root and add the following line:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### Step 3: Run the App

To start the app, use the following command:

```bash
streamlit run app.py
```

This will open the app in your default browser.

## How to Use

1. **Upload an Image**: Click on the file uploader to upload a JPEG or PNG image.
2. **Enter a Query**: Provide a query in the text input box. For example, you can ask Gemini AI to extract text, analyze the content, or provide detailed insights about the image.
3. **Analyze**: Click the "Analyze with Gemini AI" button to process the image.
4. **View Results**: The analysis results will be displayed below the upload section. You will also have the option to download the analysis results as a `.txt` file.

## Code Walkthrough

### Page Configuration

The app is set up with a custom theme using Streamlit's `set_page_config` method, providing a wide layout and a custom title and icon.

```python
st.set_page_config(
    page_title="Gemini Vision Pro",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### Sidebar with Information

The sidebar includes basic information about the app and its features, along with a footer indicating the app's creators.

```python
with st.sidebar:
    st.title("🔮 Gemini Vision Pro")
    st.markdown("---")
    st.subheader("About")
    st.markdown("""
        Transform your images into insights with Gemini Vision Pro - powered by Google's 
        advanced gemini-2.0-flash-exp model for lightning-fast image analysis.
    """)
    st.markdown("---")
    st.caption("Powered by Gemini AI 2.0")
```

### Image Upload and Analysis

The user uploads an image, which is processed by Gemini AI. The user can also input a query about the image.

```python
uploaded_file = st.file_uploader(
    "Upload Image (JPEG/PNG)",
    type=["jpg", "jpeg", "png"],
    help="Drag and drop or click to upload"
)

if st.button("🔍 Analyze with Gemini AI", key="analyze"):
    # Image and query processing
    response = get_gemini_response(detailed_prompt, image_data, input_prompt)
    st.success("✨ Analysis Complete!")
    st.markdown("### 📊 Analysis Results")
    st.markdown(response)
```

### Custom Styling

Custom CSS is applied to improve the user interface, such as customizing button styles, input fields, and image display.

```python
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
```

## Contribution

Feel free to contribute by submitting issues or pull requests. If you have any suggestions or encounter any bugs, please open an issue on the [GitHub repository](https://github.com/your-repo-link).

## License

This project is licensed under the MIT License.

---

**Created with ❤️ using Streamlit and Gemini AI**
