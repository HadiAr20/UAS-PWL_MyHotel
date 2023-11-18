import { EditKamar, ListKamar } from './pages';
import { Routes, Route } from 'react-router-dom';
// import './App.css'

function App() {

  return (
    <Routes>
        <Route path="/" element={<ListKamar/>} />
        <Route path="/edit" element={<EditKamar/>} />
    </Routes>
);
}

export default App