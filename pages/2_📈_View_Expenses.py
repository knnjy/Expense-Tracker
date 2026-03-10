"""Page for viewing and filtering expenses."""
import streamlit as st
from utils import (
    initialize_session_state,
    get_all_expenses,
    get_total_spending,
    filter_by_category,
    get_filtered_total,
    get_unique_categories,
    CATEGORIES
)

st.set_page_config(
    page_title="View Expenses | Expense Tracker",
    page_icon="💸",
    layout="wide"
)

# Initialize session state
initialize_session_state()

st.title("📊 View Expenses")

# Display all expenses
df = get_all_expenses()

if df.empty:
    st.info("📭 No expenses added yet. Start by adding an expense!")
else:
    # Display all expenses table
    st.subheader("All Expenses")
    st.dataframe(df, use_container_width=True)
    
    # Display total spending
    total = get_total_spending()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("💰 Total Spending", f"${total:.2f}")
    
    # Interactive filter section
    st.divider()
    st.subheader("🔍 Filter by Category")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        category_filter = st.selectbox(
            "Select Category",
            ["All"] + CATEGORIES,
            key="category_filter"
        )
    
    if category_filter != "All":
        filtered_df = filter_by_category(category_filter)
        
        if not filtered_df.empty:
            with col2:
                st.metric("📌 Category Total", f"${get_filtered_total(category_filter):.2f}")
            
            st.subheader(f"Expenses in {category_filter}")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.info(f"No expenses found in {category_filter} category.")
