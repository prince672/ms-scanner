import streamlit as st
import cv2
import numpy as np
import time

# --- APP CONFIG ---
st.set_page_config(page_title="M&S Scan", page_icon="🛍️", layout="wide")

# --- HIDE STREAMLIT UI (Make it look like a native app) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 0rem;} /* Remove top padding */
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- UI LAYER ---
# Display your Canva background (optional)
# st.image("bg.png", use_column_width=True)

st.title("M&S Scan & Go 🛍️")
st.markdown("### Point camera at product barcode")

# --- CAMERA INPUT ---
img_file_buffer = st.camera_input("Scan Barcode", label_visibility="hidden")

if img_file_buffer is not None:
    # Convert the file to an opencv image
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # In a real app, we would use pyzbar here to decode the barcode.
    # For this DEMO, we assume if a picture is taken, it's the correct product.
    
    with st.spinner("Processing Barcode..."):
        time.sleep(1.5) # Fake processing time
        
    st.success("Product Found: Winter Jacket!")
    time.sleep(1)
    
    # --- REDIRECT TO BILL ---
    st.switch_page("pages/bill.py")