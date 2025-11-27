import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import ArtistList from './pages/ArtistList';
import ArtistDetail from './pages/ArtistDetail';
import UserInput from './pages/UserInput';
import MatchingResults from './pages/MatchingResults';
import Roadmap from './pages/Roadmap';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/artists" element={<ArtistList />} />
          <Route path="/artists/:id" element={<ArtistDetail />} />
          <Route path="/start" element={<UserInput />} />
          <Route path="/matches" element={<MatchingResults />} />
          <Route path="/roadmap" element={<Roadmap />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
