from finance_agent_groq.schema import FinanceState
from finance_agent_groq.persistence import get_past_transactions
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

# Initialize LLM with explicit key
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, groq_api_key=os.environ.get("GROQ_API_KEY"))

def intake_node(state: FinanceState) -> FinanceState:
    print("--- Auto-Intake ---")
    return {
        **state,
        "user_name": state.get("user_name") or "Guest",
        "expense_description": state.get("expense_description") or "N/A",
        "amount": state.get("amount") or 0.0
    }

def analysis_node(state: FinanceState) -> FinanceState:
    print("--- Analyzing Expense with LLM ---")
    prompt = f"Categorize this expense: {state['expense_description']} of {state['amount']}. Respond with one word (e.g., Food, Utility, Entertainment)."
    response = llm.invoke([HumanMessage(content=prompt)])
    return {**state, "category": response.content.strip()}

def advice_node(state: FinanceState) -> FinanceState:
    print("--- Generating Advice with LLM & History ---")
    history = get_past_transactions(state["user_name"])
    history_str = "\n".join([f"- {h[0]}: ${h[1]} ({h[2]})" for h in history])
    
    prompt = f"""User: {state['user_name']}
New Expense: {state['amount']} on {state['expense_description']} (Category: {state['category']})
Past Transactions:
{history_str}

Provide brief 1-sentence financial advice based on this history."""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {**state, "advice": response.content.strip()}
