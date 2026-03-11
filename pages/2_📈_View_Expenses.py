"""Page for viewing and filtering expenses."""
from datetime import datetime

import streamlit as st
from utils import (
    initialize_session_state,
    get_all_expenses,
    get_total_spending,
    filter_by_category,
    get_filtered_total,
    get_unique_categories,
    get_archived_expenses,
    edit_expense,
    delete_expense,
    restore_expense,
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

# Tab for active and archived expenses
tab1, tab2 = st.tabs(["📝 Active Expenses", "🗂️ Archived Expenses"])

with tab1:
    # Display all expenses
    df = get_all_expenses()
    
    if df.empty:
        st.info("📭 No expenses added yet. Start by adding an expense!")
    else:
        # Display all expenses table
        st.subheader("All Expenses")
        
        # Create a display dataframe without Status column
        display_df = df[["Date", "Category", "Description", "Amount"]].copy()
        st.dataframe(display_df, use_container_width=True)
        
        # Display total spending
        total = get_total_spending()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("💰 Total Spending", f"₱{total:.2f}")
        
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
                    st.metric("📌 Category Total", f"₱{get_filtered_total(category_filter):.2f}")
                
                st.subheader(f"Expenses in {category_filter}")
                filtered_display_df = filtered_df[["Date", "Category", "Description", "Amount"]].copy()
                st.dataframe(filtered_display_df, use_container_width=True)
            else:
                st.info(f"No expenses found in {category_filter} category.")
        
        # Edit and Delete Section
        st.divider()
        st.subheader("✏️ Edit or Delete Expenses")
        
        # Get all active expenses with index
        all_expenses = st.session_state.expenses[st.session_state.expenses["Status"] == "active"].copy()
        all_expenses_reset = all_expenses.reset_index(drop=True)
        
        # Create a list of expense descriptions for selection
        expense_options = [
            f"{row['Date']} - {row['Category']}: {row['Description']} (₱{row['Amount']:.2f})"
            for _, row in all_expenses_reset.iterrows()
        ]
        
        selected_expense_idx = st.selectbox(
            "Select an expense to edit or delete",
            range(len(expense_options)),
            format_func=lambda i: expense_options[i] if i < len(expense_options) else "No expenses",
            key="expense_selector"
        )
        
        if len(all_expenses_reset) > 0:
            selected_expense = all_expenses_reset.iloc[selected_expense_idx]
            original_index = all_expenses.index[selected_expense_idx]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📋 Edit Expense Details")
                
                with st.form("edit_expense_form"):
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        edit_date = st.date_input(
                            "Date",
                            value=selected_expense["Date"],
                            key="edit_date",
                            max_value=datetime.today()
                        )
                    
                    with col_b:
                        edit_category = st.selectbox(
                            "Category",
                            CATEGORIES,
                            index=CATEGORIES.index(selected_expense["Category"]),
                            key="edit_category"
                        )
                    
                    edit_description = st.text_input(
                        "Description",
                        value=selected_expense["Description"],
                        key="edit_description"
                    )
                    
                    edit_amount = st.number_input(
                        "Amount",
                        value=float(selected_expense["Amount"]),
                        min_value=0.0,
                        format="%.2f",
                        key="edit_amount"
                    )
                    
                    col_submit1, col_submit2 = st.columns(2)
                    with col_submit1:
                        update_btn = st.form_submit_button("💾 Update Expense", use_container_width=True)
                    
                    if update_btn:
                        if edit_expense(original_index, edit_date, edit_category, edit_description, edit_amount):
                            st.success(f"✨ Updated: {edit_category} - {edit_description} (₱{edit_amount:.2f})")
                            # st.rerun()
                        else:
                            st.error("❌ Please complete all fields (description cannot be empty and amount must be greater than 0).")
            
            with col2:
                st.subheader("⚠️ Delete Expense")
                st.write(f"**Amount:** ₱{selected_expense['Amount']:.2f}")
                
                if st.button("🗑️ Delete (Archive)", use_container_width=True):
                    if delete_expense(original_index):
                        st.success(f"✋ Archived: {selected_expense['Category']} - {selected_expense['Description']} (₱{selected_expense['Amount']:.2f})")
                        # st.rerun()
                    else:
                        st.error("❌ Failed to delete expense.")

with tab2:
    archived_df = get_archived_expenses()
    
    if archived_df.empty:
        st.info("🗂️ No archived expenses yet.")
    else:
        st.subheader("Archived Expenses")
        
        # Display archived expenses
        display_archived_df = archived_df[["Date", "Category", "Description", "Amount"]].copy()
        st.dataframe(display_archived_df, use_container_width=True)
        
        # Restore archived expenses
        st.divider()
        st.subheader("🔄 Restore Expenses")
        
        archived_expenses_reset = archived_df.reset_index(drop=True)
        
        # Create a list of archived expense descriptions for selection
        archived_expense_options = [
            f"{row['Date']} - {row['Category']}: {row['Description']} (₱{row['Amount']:.2f})"
            for _, row in archived_expenses_reset.iterrows()
        ]
        
        selected_archived_idx = st.selectbox(
            "Select an archived expense to restore",
            range(len(archived_expense_options)),
            format_func=lambda i: archived_expense_options[i] if i < len(archived_expense_options) else "No archived expenses",
            key="archived_expense_selector"
        )
        
        if len(archived_expenses_reset) > 0:
            selected_archived = archived_expenses_reset.iloc[selected_archived_idx]
            original_archived_index = archived_df.index[selected_archived_idx]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Date:** {selected_archived['Date']}")
                st.write(f"**Category:** {selected_archived['Category']}")
                st.write(f"**Description:** {selected_archived['Description']}")
                st.write(f"**Amount:** ₱{selected_archived['Amount']:.2f}")
            
            with col2:
                if st.button("↩️ Restore", use_container_width=True):
                    if restore_expense(original_archived_index):
                        st.success(f"↩️ Restored: {selected_archived['Category']} - {selected_archived['Description']} (₱{selected_archived['Amount']:.2f})")
                        # st.rerun()
                    else:
                        st.error("❌ Failed to restore expense.")
