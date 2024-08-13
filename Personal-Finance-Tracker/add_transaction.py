import streamlit as st
import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        st.success("Entry added successfully")

def app():
    CSV.initialize_csv()
    st.title("Add Transaction")

    date = st.date_input("Date", datetime.today()).strftime("%d-%m-%Y")
    amount = st.number_input("Amount", min_value=0.01)
    category = st.selectbox("Category", ["Income", "Expense"])
    description = st.text_input("Description (optional)")

    if st.button("Add Entry"):
        CSV.add_entry(date, amount, category, description)
