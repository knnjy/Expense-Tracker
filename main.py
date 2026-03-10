"""
Expense Tracker - Multi-Page Streamlit Application
Main entry point for the application.
"""
import streamlit as st
import pandas as pd
from utils import (
    get_total_spending,
    get_all_expenses,
    get_spending_by_category,
    get_spending_over_time,
    initialize_session_state
)


# Configure page settings
st.set_page_config(
    page_title="Dashboard | Expense Tracker",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_session_state()

# ========== DASHBOARD CONTENT ==========
st.title("💸 Expense Tracker ni Ken")
st.markdown(
    """
    Welcome to your personal expense tracker! 📊
    
    ### Features:
    - 📝 **Add Expense** - Record your daily spending
    - 📈 **View Expenses** - Analyze spending by category
    - 📖 **About** - Learn more about the app
    
    Use the navigation menu on the left to get started!
    """
)

st.divider()

# Quick Stats Section
st.subheader("📈 Quick Statistics")

try:
    total = get_total_spending()
    expense_count = len(get_all_expenses())
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Total Spending", f"${total:.2f}")
    with col2:
        st.metric("📝 Total Expenses", expense_count)
    with col3:
        avg_expense = (total / expense_count) if expense_count > 0 else 0
        st.metric("📊 Average Expense", f"${avg_expense:.2f}")
    
    st.divider()
    
    # Charts Section
    if expense_count > 0:
        chart_col1, chart_col2 = st.columns(2)
        
        # Spending by Category - Bar Chart
        with chart_col1:
            st.subheader("📊 Spending by Category")
            category_data = get_spending_by_category()
            
            if not category_data.empty:
                st.bar_chart(
                    data=category_data.set_index("Category"),
                    use_container_width=True
                )
            else:
                st.info("No category data available yet.")
        
        # Spending Over Time - Line Chart
        with chart_col2:
            st.subheader("📈 Spending Over Time")
            time_data = get_spending_over_time()
            
            if not time_data.empty:
                st.line_chart(
                    data=time_data.set_index("Date"),
                    use_container_width=True
                )
            else:
                st.info("No time series data available yet.")
    else:
        st.info("Start by adding an expense to see statistics and charts!")
        
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.info("Make sure to add some expenses first!")