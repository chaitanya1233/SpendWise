import sqlite3
from finance_agent_groq.schema import FinanceState

DB_PATH = "finance_data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            description TEXT,
            amount REAL,
            category TEXT,
            advice TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_transaction_node(state: FinanceState) -> FinanceState:
    print("--- Saving to SQLite ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (user_name, description, amount, category, advice) VALUES (?, ?, ?, ?, ?)",
        (state["user_name"], state["expense_description"], state["amount"], state["category"], state["advice"])
    )
    transaction_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {**state, "transaction_id": transaction_id}

def get_past_transactions(user_name: str, limit: int = 3):
    print(f"--- Fetching History for {user_name} ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT description, amount, category FROM transactions WHERE user_name = ? ORDER BY id DESC LIMIT ?",
        (user_name, limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
