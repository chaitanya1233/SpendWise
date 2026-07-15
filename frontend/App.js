import React, { useState } from 'react';

function App() {
  const [data, setData] = useState({ user_name: '', expense_description: '', amount: '' });
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://localhost:8000/triage_expense', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    const json = await response.json();
    setResult(json);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>SpendWise AI</h1>
      <form onSubmit={handleSubmit}>
        <input placeholder="Name" onChange={e => setData({...data, user_name: e.target.value})} />
        <input placeholder="Expense" onChange={e => setData({...data, expense_description: e.target.value})} />
        <input placeholder="Amount" type="number" onChange={e => setData({...data, amount: parseFloat(e.target.value)})} />
        <button type="submit">Get Advice</button>
      </form>
      {result && (
        <div>
          <h3>Category: {result.category}</h3>
          <p>Advice: {result.advice}</p>
        </div>
      )}
    </div>
  );
}
export default App;
