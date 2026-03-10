"""Page for adding new expenses."""
import streamlit as st
from datetime import datetime
from utils import (
    initialize_session_state,
    add_expense,
    CATEGORIES
)

st.set_page_config(
    page_title="Add Expense | Expense Tracker",
    page_icon="💸",
    layout="wide"
)

# Initialize session state
initialize_session_state()

st.title("📝 Add New Expense")

with st.form("expense_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        date = st.date_input("Date", datetime.today())
    
    with col2:
        category = st.selectbox("Category", CATEGORIES)
    
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    
    submitted = st.form_submit_button("✅ Add Expense", use_container_width=True)

if submitted:
    if add_expense(date, category, description, amount):
        st.success("✨ Expense added successfully!")
        st.balloons()
    else:
        st.error("❌ Please complete all fields (description cannot be empty and amount must be greater than 0).")
