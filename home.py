import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Scan & Go", page_icon="🛍️", layout="wide")

# --- CUSTOM CSS (The "Gen Z" styling) ---
st.markdown("""
    <style>
        /* Hide Streamlit Header/Footer */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Remove top padding to make it full screen */
        .block-container {
            padding-top: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        
        /* Hide the camera switcher button (small icon) */
        button[title="Switch camera"] {
            display: none;
        }
        
        /* Center the camera title */
        h1 {
            text-align: center;
            font-family: sans-serif;
            font-size: 24px;
            padding-top: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# --- APP CONTENT ---
st.title("Scan Item 📸")

# --- CAMERA ---
# We use a container to keep it centered if on desktop, but full on mobile
with st.container():
    img_file_buffer = st.camera_input("Scanner", label_visibility="hidden")

if img_file_buffer is not None:
    # Fake processing
    with st.spinner("Identifying product..."):
        time.sleep(1.2)
    
    # Redirect to Bill
    st.switch_page("pages/bill.py")