import streamlit as st
import time

st.set_page_config(page_title="Scan", page_icon="📸", layout="wide")

# Inject JS to force back camera
st.markdown("""
<script>
navigator.mediaDevices.getUserMedia = (constraints) => {
    constraints = constraints || {};
    constraints.video = constraints.video || {};
    constraints.video.facingMode = { exact: "environment" }; // FORCE BACK CAMERA
    return navigator.mediaDevices.__proto__.getUserMedia.call(navigator.mediaDevices, constraints);
}
</script>
""", unsafe_allow_html=True)


# CSS for fullscreen camera & no switch button
st.markdown("""
<style>

    #MainMenu, footer, header {visibility: hidden !important;}

    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
    }

    [data-testid="stCameraInput"] {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stCameraInput"] > div {
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Fullscreen video */
    [data-testid="stCameraInput"] video {
        width: 100vw !important;
        height: 88vh !important;
        object-fit: cover !important;
        border-radius: 0 !important;
        background: #000 !important;
    }

    /* Hide camera switch button */
    [data-testid="stCameraInput"] button {
        display: none !important;
    }

    label { display: none !important; }

</style>
""", unsafe_allow_html=True)



# CAMERA WIDGET
img = st.camera_input("scanner", label_visibility="hidden")

if img is not None:
    with st.spinner("Processing..."):
        time.sleep(0.6)
    st.switch_page("pages/bill.py")
