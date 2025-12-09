import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="M&S Scan", page_icon="🛍️", layout="wide")

# --- HIDE STREAMLIT UI (Makes it look like a real app) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 1rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- TITLE ---
st.title("Scan & Go 🛍️")
st.caption("Point your camera at the barcode")

# --- THE CAMERA ---
# This widget turns on the camera.
# As soon as you snap a photo, 'img_file_buffer' gets data.
img_file_buffer = st.camera_input("Scan Barcode", label_visibility="hidden")

# --- THE REDIRECT LOGIC ---
if img_file_buffer is not None:
    # If a picture is taken, we assume the code was scanned successfully.
    
    # 1. Show a quick spinner so the user feels "processing" is happening
    with st.spinner("Processing Barcode..."):
        time.sleep(1.2) # Fake delay
    
    # 2. Show Success
    st.success("Item Detected: Winter Jacket")
    time.sleep(0.5)
    
    # 3. TRIGGER THE REDIRECT (This is the magic line)
    st.switch_page("pages/bill.py")