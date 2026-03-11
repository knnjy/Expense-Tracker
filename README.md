# 💸 Expense Tracker

A simple yet powerful Streamlit application for personal finance management and expense tracking in Philippine Pesos (₱).

## 📋 Features

### Core Functionality
- **📝 Add Expenses** - Record daily expenses with date, category, description, and amount
- **✏️ Edit Expenses** - Update existing expense details anytime
- **🗑️ Delete (Archive)** - Soft delete expenses while preserving data
- **↩️ Restore** - Recover archived expenses back to active
- **🔍 Filter by Category** - View expenses by Food, Transport, Shopping, Bills, or Other

### Analytics & Insights
- **📊 Dashboard** - Quick statistics (total spending, expense count, average)
- **📈 Charts** - Visualize spending by category (bar chart) and over time (line chart)
- **💰 Category Analysis** - Track spending totals per category
- **📑 Archived View** - Complete history of deleted expenses

## 🛠️ Tech Stack

- **Python 3.13**
- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **Session State** - In-app data storage

## 📦 Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📂 File Structure

- `Home.py`                 # Dashboard & entry point
- `pages/`
  - `1_📝_Add_Expense.py`    # Add expenses
  - `2_📈_View_Expenses.py`  # View expenses
  - `3_📖_About.py`          # About the app
- `utils.py`               # Helper functions
- `requirements.txt`       # Dependencies
- `README.md`             # This file

📖 Pages & Navigation
🏠 Dashboard (Home)
- Quick statistics overview
- Visual charts (spending by category and trends)
- Navigation guidance to other pages
📝 Add Expense
- Form to record new expenses
- Select date, category, description, and amount
- Real-time success feedback
📈 View Expenses
Active Expenses Tab

- View all expenses in table format
- Filter by category
- Edit expense details
- Delete (archive) expenses
Archived Expenses Tab

- View all deleted expenses
- Restore any archived expense
📖 About
- Complete feature documentation
- App capabilities and functionality
- Getting started guide
💡 Quick Start Guide
1. Add an Expense

- Go to "Add Expense" page
- Fill in Date, Category, Description, Amount
- Click "Add Expense"
2. View & Manage

- Go to "View Expenses" page
- See all expenses in table
- Use filters to view by category
- Edit or delete as needed
3. Analyze

- Check Dashboard for statistics
- View charts for spending patterns
- Compare spending by category
4. Restore

- Go to "View Expenses" → Archived tab
- Select expense to restore
- Click "Restore" button
📊 Expense Categories
    🍔 Food - Dining, groceries
    🚗 Transport - Commute, fuel, rides
    🛍️ Shopping - Clothes, items
    💳 Bills - Utilities, subscriptions
    📌 Other - Miscellaneous

💳 Currency
All amounts are in Philippine Pesos (₱)

🔄 Session Management
The app uses Streamlit's session state to persist data during the session. Expenses are stored in memory while the app is running.

📝 Notes
    All delete operations are soft deletes - data is archived, not permanently removed
    You can restore any archived expense anytime
    Changes take effect immediately with visual feedback

🤝 Contributing
Feel free to fork, modify, and improve!

📄 License

Open source - feel free to use and modify
