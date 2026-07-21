from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from finance_agent_groq.graph import graph
import os

app = FastAPI()

# CORS Middleware
origins = [
    "http://localhost:3000",
    "https://spendwise-frontend.vercel.app" # Replace with your actual Vercel domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "running", "service": "SpendWise API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

class ExpenseInput(BaseModel):
    user_name: str
    expense_description: str
    amount: float

@app.post("/analyze")
async def analyze_expense(data: ExpenseInput):
    result = graph.invoke(data.dict())
    return {"advice": result.get("advice"), "category": result.get("category")}
