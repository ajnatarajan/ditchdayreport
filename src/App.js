import Navbar from "./components/Navbar";
import Leaderboard from "./components/Leaderboard";
import ReportSection from "./components/ReportSection";
import "./App.css";

function App() {
  return (
    <div className="app">
      <Navbar />
      <Leaderboard />
      <ReportSection />
    </div>
  );
}

export default App;
