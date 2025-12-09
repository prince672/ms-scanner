import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Scan", page_icon="📸", layout="wide")

# --- NUCLEAR CSS (Force Full Screen Mobile Look) ---
st.markdown("""
    <style>
        /* 1. HIDE ALL STREAMLIT UI ELEMENTS */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* 2. REMOVE ALL PADDING (Full Bleed) */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        /* 3. CAMERA CONTAINER STYLING */
        [data-testid="stCameraInput"] {
            width: 100% !important;
            border: none !important;
            background-color: black !important;
        }
        
        /* 4. FORCE VIDEO TO BE TALL (The "App" Look) */
        video {
            width: 100% !important;
            height: 80vh !important; /* Takes up 80% of screen height */
            object-fit: cover !important; /* Zoom to fill screen without stretching */
            border-radius: 0px !important;
        }
        
        /* 5. HIDE THE SWITCH CAMERA BUTTON */
        /* We target the button inside the camera widget specifically */
        div[data-testid="stCameraInput"] > div > div > button {
            display: none !important;
        }
        
        /* 6. HIDE THE SMALL "Take Photo" LABEL IF VISIBLE */
        label {
            display: none !important;
        }

    </style>
    """, unsafe_allow_html=True)

# --- THE CAMERA WIDGET ---
# We put it directly on the page, no columns, no containers
img_file_buffer = st.camera_input("Scanner", label_visibility="hidden")

# --- REDIRECT LOGIC ---
if img_file_buffer is not None:
    # Fake processing spinner
    with st.spinner("Processing..."):
        time.sleep(0.8)
    
    # Redirect immediately
    st.switch_page("pages/bill.py")