import { useState } from 'react'
import { algorithms } from './algorithms'
import './App.css'

export default function App() {
  const [selectedId, setSelectedId] = useState(algorithms[0].id)
  const selected = algorithms.find((a) => a.id === selectedId) ?? algorithms[0]

  return (
    <main className="app">
      <h1>Algorithm Visualizer</h1>

      <label className="picker">
        Algorithm
        <select value={selectedId} onChange={(e) => setSelectedId(e.target.value)}>
          {algorithms.map((a) => (
            <option key={a.id} value={a.id}>
              {a.name}
            </option>
          ))}
        </select>
      </label>

      <video key={selected.video} className="player" src={selected.video} controls autoPlay loop muted />

      <p className="complexity">Time complexity: {selected.complexity}</p>
      <p>{selected.description}</p>
    </main>
  )
}
