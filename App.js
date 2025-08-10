import React, { useState } from 'react';
import Header from './components/Header';
import CaseForm from './components/CaseForm';
import Dashboard from './components/Dashboard';
import AISummary from './components/AISummary';
import './index.css';

function App() {
  const [showForm, setShowForm] = useState(false);
  const [showSummary, setShowSummary] = useState(false);
  const [cases, setCases] = useState([]);
  const [currentCase, setCurrentCase] = useState(null);

  const addCase = (newCase) => {
    setCases([...cases, newCase]);
    setCurrentCase(newCase);
    setShowSummary(true);
  };

  return (
    <div className="app">
      <Header onNewCase={() => setShowForm(true)} />

      {showForm && (
        <CaseForm
          onCancel={() => setShowForm(false)}
          onSubmit={addCase}
        />
      )}

      <Dashboard cases={cases} />

      {showSummary && currentCase && (
        <AISummary
          surgicalCase={currentCase}
          onClose={() => setShowSummary(false)}
        />
      )}
    </div>
  );
}

export default App;
