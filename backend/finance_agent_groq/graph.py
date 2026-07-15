from langgraph.graph import StateGraph, END
from finance_agent_groq.schema import FinanceState
from finance_agent_groq.nodes import intake_node, analysis_node, advice_node
from finance_agent_groq.persistence import save_transaction_node, init_db

# Ensure DB is ready
init_db()

# Build the Graph
builder = StateGraph(FinanceState)

# Add Nodes
builder.add_node("intake", intake_node)
builder.add_node("analysis", analysis_node)
builder.add_node("advice", advice_node)
builder.add_node("save", save_transaction_node)

# Set Entry and Edges
builder.set_entry_point("intake")
builder.add_edge("intake", "analysis")
builder.add_edge("analysis", "advice")
builder.add_edge("advice", "save")
builder.add_edge("save", END)

# Compile
graph = builder.compile()
