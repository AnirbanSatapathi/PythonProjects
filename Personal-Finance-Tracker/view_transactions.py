import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=cls.FORMAT)
        start_date = datetime.strptime(start_date, cls.FORMAT)
        end_date = datetime.strptime(end_date, cls.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        return filtered_df


def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

def app():
    st.title("View Transactions")

    start_date = st.date_input("Start Date", datetime.today()).strftime("%d-%m-%Y")
    end_date = st.date_input("End Date", datetime.today()).strftime("%d-%m-%Y")

    if st.button("Get Transactions"):
        df = CSV.get_transactions(start_date, end_date)
        if df.empty:
            st.write("No transactions found in the given date range.")
        else:
            # Format the date column to show only the date part
            df["date"] = df["date"].dt.strftime("%d-%m-%Y")
            st.write(df)

            # Calculate and display the summary
            total_income = df[df["category"] == "Income"]["amount"].sum()
            total_expense = df[df["category"] == "Expense"]["amount"].sum()
            net_savings = total_income - total_expense

            st.write("Summary:")
            st.write(f"Total Income: ${total_income:.2f}")
            st.write(f"Total Expense: ${total_expense:.2f}")
            st.write(f"Net Savings: ${net_savings:.2f}")

            # Plot the transactions
            if st.checkbox("Show Plot"):
                plt.show(plot_transactions(df))
