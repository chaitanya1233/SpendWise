from typing import TypedDict, Optional

class FinanceState(TypedDict):
    user_name: str
    expense_description: str
    amount: float
    category: Optional[str]
    advice: Optional[str]
    is_over_budget: bool
    transaction_id: Optional[int] # Added to track DB record
