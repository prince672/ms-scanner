import streamlit as st
import time
import random

st.set_page_config(page_title="Bill", layout="centered")

# --- CSS FOR CLEAN LOOK ---
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {padding-top: 2rem;}
        
        /* Style for the 'Paper Invoice' look */
        .invoice-box {
            background-color: white;
            padding: 30px;
            border: 1px dashed #ccc;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            font-family: 'Courier New', Courier, monospace;
            color: black;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if "billed" not in st.session_state:
    st.session_state.billed = False

# --- SCREEN 1: GET DETAILS ---
if not st.session_state.billed:
    st.markdown("<br><br>", unsafe_allow_html=True) # Spacing
    st.title("Complete Purchase")
    
    with st.form("billing_form"):
        name = st.text_input("Enter Customer Name", placeholder="e.g. Prince")
        submitted = st.form_submit_button("Generate Bill", type="primary", use_container_width=True)
        
        if submitted and name:
            st.session_state.customer_name = name
            st.session_state.billed = True
            st.rerun()

# --- SCREEN 2: THE RECEIPT ---
else:
    # Generate random invoice details
    inv_no = random.randint(1000, 9999)
    date = time.strftime("%d/%m/%Y %H:%M")
    
    # HTML Invoice for that "Real Paper" feel
    invoice_html = f"""
    <div class="invoice-box">
        <center>
            <h3>MARKS & SPENCER</h3>
            <p>High Street, Mumbai Store</p>
            <hr>
        </center>
        <p><strong>Date:</strong> {date}</p>
        <p><strong>Bill To:</strong> {st.session_state.customer_name}</p>
        <p><strong>Inv No:</strong> MS-{inv_no}</p>
        <hr>
        <table style="width:100%">
            <tr>
                <td style="text-align:left">Winter Puffer Jacket</td>
                <td style="text-align:right">₹4,500.00</td>
            </tr>
            <tr>
                <td style="text-align:left">Tax (18%)</td>
                <td style="text-align:right">₹810.00</td>
            </tr>
            <tr><td colspan="2"><hr></td></tr>
            <tr style="font-weight:bold; font-size:18px">
                <td style="text-align:left">TOTAL</td>
                <td style="text-align:right">₹5,310.00</td>
            </tr>
        </table>
        <hr>
        <center>
            <p>Paid via UPI (Success)</p>
            <p style="font-size:10px">Thank you for shopping with us!</p>
            <p style="font-size:20px">barcode_here_||||||</p>
        </center>
    </div>
    """
    st.markdown(invoice_html, unsafe_allow_html=True)

    # --- BUTTON: BACK TO CANVA ---
    # Replace this link with your ACTUAL Canva prototype link
    canva_link = "https://markndspencer.my.canva.site/page-2" 
    
    st.link_button("⬅ Back to App Menu", canva_link, type="secondary", use_container_width=True)