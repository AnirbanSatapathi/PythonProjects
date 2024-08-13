import streamlit as st

# Define the pages
pages = {
    "Add Transaction": "add_transaction",
    "View Transactions": "view_transactions",
}

# Sidebar for navigation
st.sidebar.title("Finance Tracker")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
if selection == "Add Transaction":
    from add_transaction import app as add_transaction_app
    add_transaction_app()
elif selection == "View Transactions":
    from view_transactions import app as view_transactions_app
    view_transactions_app()
