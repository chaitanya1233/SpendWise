import React, { useState } from 'react';

const styles = {
  page: {
    minHeight: '100vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%)',
    padding: '20px'
  },
  container: {
    width: '100%',
    maxWidth: '450px',
    padding: '40px',
    borderRadius: '24px',
    background: 'rgba(255, 255, 255, 0.05)',
    backdropFilter: 'blur(10px)',
    border: '1px solid rgba(255, 255, 255, 0.1)',
    color: 'white',
    boxShadow: '0 20px 40px rgba(0,0,0,0.3)'
  },
  input: {
    width: '100%',
    padding: '14px',
    margin: '12px 0',
    borderRadius: '12px',
    border: '1px solid rgba(255, 255, 255, 0.2)',
    background: 'rgba(255, 255, 255, 0.1)',
    color: 'white',
    fontSize: '16px',
    boxSizing: 'border-box'
  },
  button: {
    width: '100%',
    padding: '16px',
    background: 'linear-gradient(90deg, #6366f1 0%, #a855f7 100%)',
    color: 'white',
    border: 'none',
    borderRadius: '12px',
    fontSize: '18px',
    fontWeight: 'bold',
    cursor: 'pointer',
    marginTop: '20px',
    transition: 'transform 0.2s'
  },
  result: {
    marginTop: '30px',
    padding: '20px',
    background: 'rgba(255, 255, 255, 0.1)',
    borderRadius: '16px',
    borderLeft: '4px solid #a855f7'
  }
};

function App() {
  const [data, setData] = useState({ user_name: '', expense_description: '', amount: '' });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
      try {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/analyze`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });
        if (!response.ok) throw new Error('Network response was not ok');
        const json = await response.json();
        setResult(json);
      } catch (err) { alert("Backend connection failed: " + err.message); }

    setLoading(false);
  };

  return (
    <div style={styles.page}>
      <div style={styles.container}>
        <h1 style={{ textAlign: 'center', margin: '0 0 30px 0', fontSize: '28px' }}>SpendWise AI ✨</h1>
        <form onSubmit={handleSubmit}>
          <input style={styles.input} placeholder="Your Name" onChange={e => setData({...data, user_name: e.target.value})} />
          <input style={styles.input} placeholder="What did you spend on?" onChange={e => setData({...data, expense_description: e.target.value})} />
          <input style={styles.input} placeholder="Amount ($)" type="number" onChange={e => setData({...data, amount: parseFloat(e.target.value)})} />
          <button style={styles.button} type="submit" disabled={loading}>
            {loading ? 'Crunching data...' : 'Get Financial Advice'}
          </button>
        </form>
        {result && (
          <div style={styles.result}>
            <h3 style={{ margin: '0 0 10px 0', color: '#a855f7' }}>{result.category}</h3>
            <p style={{ margin: 0, fontSize: '15px', lineHeight: '1.5' }}>{result.advice}</p>
          </div>
        )}
      </div>
    </div>
  );
}
export default App;
