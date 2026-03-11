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
    
    - 📝 **Record** daily expenses with detailed information (date, category, description, amount)
    - ✏️ **Edit** existing expenses to correct or update information
    - 🗑️ **Delete (Archive)** expenses - soft delete that keeps data for recovery
    - ↩️ **Restore** archived expenses back to active
    - 📊 **Analyze** spending patterns by category
    - 📈 **Visualize** spending trends over time
    - 💰 **Monitor** total spending at a glance
    - 🔍 **Filter** and review expenses by category
    - 📑 **View archived expenses** history anytime
    
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
        - **Amount** - How much was spent (in Philippine Pesos ₱)
        """
    )

with col2:
    st.subheader("What It Shows (Outputs)")
    st.markdown(
        """
        - **Dashboard Statistics**
          - Total spending across all expenses
          - Number of expenses recorded
          - Average expense amount
          - Category breakdown
        
        - **Visual Analytics**
          - Bar chart: Spending by category
          - Line chart: Spending trends over time
        
        - **Detailed Views**
          - Complete active expense table
          - Filtered views by category
          - Category-specific totals
          - Archived expenses
          - Restore functionality
        """
    )

st.divider()

# Features Section
st.header("Key Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    st.subheader("✏️ Full Expense Management")
    st.markdown(
        """
        - **Add** expenses quickly and easily
        - **Edit** any existing expense details
        - **Delete** (archive) unwanted entries
        - **Restore** deleted expenses anytime
        - All data preserved in archive
        """
    )

with feature_col2:
    st.subheader("📊 Smart Analytics")
    st.markdown(
        """
        - **Real-time statistics** on dashboard
        - **Category breakdown** of spending
        - **Spending trends** visualized over time
        - **Filter by category** for detailed analysis
        - **Automatic calculations** of totals
        """
    )

st.divider()

st.info(
    """
    💡 **Getting Started:**
    1. Go to the **Add Expense** page to start recording your spending
    2. Use the **View Expenses** page to manage, analyze, and organize your expenses
    3. Check the **Dashboard** for quick statistics and visual insights
    4. Visit the **About** page for detailed information about features
    """
)
