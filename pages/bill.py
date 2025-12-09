import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Invoice", page_icon="🧾")

# --- HIDE DEFAULT UI (Clean App Look) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {padding-top: 2rem;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- HEADER ---
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Marks_%26_Spencer_Logo.svg/2560px-Marks_%26_Spencer_Logo.svg.png", width=150)
st.title("Self-Checkout")

# --- INPUT SECTION ---
# This asks for the name. The bill only shows AFTER they type it.
name = st.text_input("Enter Customer Name for Billing", placeholder="Type name here...")

if name:
    # Fake processing delay to make it feel real
    with st.spinner("Verifying Payment..."):
        time.sleep(1.5)

    # --- SUCCESS MESSAGE ---
    st.success("✅ Payment Successful via UPI")
    
    # --- THE INVOICE CARD ---
    st.markdown("---")
    st.subheader("OFFICIAL RECEIPT")
    
    # Random Invoice Number for realism
    inv_id = random.randint(100000, 999999)
    current_date = time.strftime("%d-%b-%Y")

    st.write(f"**Customer:** {name}")
    st.write(f"**Invoice ID:** #MS-{inv_id}")
    st.write(f"**Date:** {current_date}")
    
    st.markdown("### Items")
    
    # The Fake Items (Hardcoded for the demo)
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("1x Men's Winter Puffer Jacket")
        st.write("1x Wool Scarf (Grey)")
    with col2:
        st.write("₹4,500")
        st.write("₹1,200")

    st.markdown("---")
    
    # Total Calculation
    col3, col4 = st.columns([3, 1])
    with col3:
        st.markdown("### TOTAL PAID")
    with col4:
        st.markdown("### ₹5,700")
        
    st.caption("Tax Invoice | Marks & Spencer Pvt Ltd")
    
    st.markdown("---")

    # --- RESET BUTTON ---
    # This button takes them back to the scanner to start over
    if st.button("Scan Next Item 📷", type="primary"):
        st.switch_page("home.py")

else:
    st.info("Waiting for customer details...")