"""About page for Expense Tracker application."""
import streamlit as st

st.set_page_config(
    page_title="About | Expense Tracker",
    page_icon="💸",
    layout="wide"
)

st.title("📖 About Expense Tracker")

st.divider()

# What the app does
st.header("What the App Does")
st.markdown(
    """
    **Expense Tracker** is a personal finance management application that helps you:
    
    - 📝 Record and track daily expenses with detailed information
    - 📊 Analyze spending patterns by category
    - 📈 Visualize spending trends over time
    - 💰 Monitor total spending at a glance
    - 🔍 Filter and review expenses by category
    
    This app provides a simple yet powerful solution for personal budget management and financial awareness.
    """
)

st.divider()

# Target User
st.header("Who It's For")
st.markdown(
    """
    **Ideal for:**
    - 👤 **Individuals** who want to track their daily spending
    - 💼 **Freelancers & Self-Employed** monitoring business expenses
    - 👨‍👩‍👧‍👦 **Families** managing household budget
    - 🎓 **Students** controlling spending
    - 🏠 **Renters** tracking personal finances
    
    Anyone who wants a simple, effective way to understand where their money is going!
    """
)

st.divider()

# Inputs & Outputs
st.header("Inputs & Outputs")

col1, col2 = st.columns(2)

with col1:
    st.subheader("What It Collects (Inputs)")
    st.markdown(
        """
        - **Date** - When the expense occurred
        - **Category** - Type of expense:
          - Food
          - Transport
          - Shopping
          - Bills
          - Other
        - **Description** - Details about the expense
        - **Amount** - How much was spent (in dollars)
        """
    )

with col2:
    st.subheader("What It Shows (Outputs)")
    st.markdown(
        """
        - **Dashboard Statistics**
          - Total spending across all expenses
          - Number of expenses recorded
          - Category breakdown
        
        - **Visual Analytics**
          - Bar chart: Spending by category
          - Line chart: Spending trends over time
        
        - **Detailed Views**
          - Complete expense table
          - Filtered views by category
          - Category-specific totals
        """
    )

st.divider()

st.info(
    """
    💡 **Getting Started:**
    1. Go to the **Add Expense** page to start recording your spending
    2. Use the **View Expenses** page to analyze your spending patterns
    3. Check the **Dashboard** for quick statistics and insights
    """
)
