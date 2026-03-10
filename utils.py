"""Utility functions for Expense Tracker application."""
import pandas as pd
import streamlit as st
from datetime import datetime

# Constants
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Other"]
COLUMNS = ["Date", "Category", "Description", "Amount"]


def initialize_session_state() -> None:
    """Initialize session state for expenses if not already present."""
    if "expenses" not in st.session_state:
        st.session_state.expenses = pd.DataFrame(columns=COLUMNS)


def add_expense(
    date: datetime,
    category: str,
    description: str,
    amount: float
) -> bool:
    
    if not description or amount == 0:
        return False
    
    new_expense = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Description": [description],
        "Amount": [amount]
    })
    
    # Add the new expense to expenses
    st.session_state.expenses = pd.concat(
        [st.session_state.expenses, new_expense],
        ignore_index=True
    )
    return True

# Get all expenses from session state.
def get_all_expenses() -> pd.DataFrame:
    return st.session_state.expenses.copy()

def get_total_spending() -> float:
    """Calculate total spending across all expenses."""
    df = st.session_state.expenses
    return df["Amount"].sum() if not df.empty else 0.0

# Filter expenses by category.
def filter_by_category(category: str) -> pd.DataFrame:
    
    df = st.session_state.expenses
    if df.empty or category == "All":
        return df.copy()
    return df[df["Category"] == category]


def get_filtered_total(category: str) -> float:
    """Calculate total spending for a specific category."""
    filtered_df = filter_by_category(category)
    return filtered_df["Amount"].sum() if not filtered_df.empty else 0.0


def get_unique_categories() -> list:
    """Get list of unique categories from expenses."""
    df = st.session_state.expenses
    return list(df["Category"].unique()) if not df.empty else []


def get_spending_by_category() -> pd.DataFrame:
    # Get total spending grouped by category.

    df = st.session_state.expenses
    if df.empty:
        return pd.DataFrame(columns=["Category", "Amount"])
    
    return df.groupby("Category")["Amount"].sum().reset_index().sort_values("Amount", ascending=False)


def get_spending_over_time() -> pd.DataFrame:

    # Get daily spending over time.

    df = st.session_state.expenses
    if df.empty:
        return pd.DataFrame(columns=["Date", "Amount"])
    
    # Convert Date column to datetime if not already
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Group by date and sum amounts
    daily_spending = df.groupby("Date")["Amount"].sum().reset_index()
    return daily_spending.sort_values("Date")
