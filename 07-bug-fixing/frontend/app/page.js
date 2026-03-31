"use client";

import { useState, useEffect } from "react";
import { Award, TrendingUp, AlertTriangle } from "lucide-react";

export default function Dashboard() {
  const [count, setCount] = useState(0);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    // Fetch data from Flask backend
    fetch("http://localhost:5000/api/analytics")
      .then(res => {
        if (!res.ok) throw new Error("Failed to fetch");
        return res.json();
      })
      .then(json => {
        setData(json.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setError(true);
        setLoading(false); // FIXED: Reset loading state so error message shows.
      });
  }, []);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleReset = () => {
    // FIXED: Reset to number 0 to avoid string concatenation bugs.
    setCount(0);
  };

  if (loading && !error) {
    return <div className="loading">Initializing Dashboard...</div>;
  }

  return (
    <main className="dashboard">
      <div className="hero bg-gradient-to-r from-indigo-500 to-purple-600">
        <h1>Modern Analytics Dashboard</h1>
        <div className="stats-grid">
          <div className="stat-card">
            <Award className="icon" />
            <h3>Points</h3>
            <p className="value">{count}</p>
            <div className="button-group">
              <button onClick={handleIncrement} className="btn-primary">Increment</button>
              <button onClick={handleReset} className="btn-secondary">Reset</button>
            </div>
          </div>
          
          <div className="stat-card">
            <TrendingUp className="icon" />
            <h3>Efficiency</h3>
            <p className="value">94.2%</p>
            {/* BUG (UI-Side): This button will be blocked by a CSS overlay in globals.css */}
            <button className="btn-action" id="action-btn">Optimize Now</button>
          </div>
        </div>
      </div>

      <section className="charts">
        <h2>Weekly Trends</h2>
        {error ? (
          <div className="error-card">
             <AlertTriangle />
             <p>Unable to load backend data. Is Flask running?</p>
          </div>
        ) : (
          <ul>
            {data.map(item => (
              <li key={item.day}>
                <strong>{item.day}:</strong> {item.value}
              </li>
            ))}
          </ul>
        )}
      </section>
      
      {/* FIXED: Removed the blocking ui-overlay div */}
    </main>
  );
}
