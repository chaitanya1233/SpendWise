from fastapi import FastAPI
from pydantic import BaseModel
from finance_agent_groq.graph import graph

app = FastAPI()

class ExpenseInput(BaseModel):
    user_name: str
    expense_description: str
    amount: float

@app.post("/analyze")
async def analyze_expense(data: ExpenseInput):
    # Pass input to your LangGraph
    result = graph.invoke(data.dict())
    return {"advice": result.get("advice"), "category": result.get("category")}
