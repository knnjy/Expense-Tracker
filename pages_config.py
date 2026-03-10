"""
Pages configuration for Expense Tracker
Maps display names and icons to actual page files
"""

PAGES = [
    {
        "title": "Dashboard",
        "icon": "📊",
        "path": "main.py",
    },
    {
        "title": "Add Expense",
        "icon": "📝",
        "path": "pages/add_expense.py",
    },
    {
        "title": "View Expenses",
        "icon": "📈",
        "path": "pages/view_expenses.py",
    },
    {
        "title": "About",
        "icon": "📖",
        "path": "pages/about.py",
    },
]
