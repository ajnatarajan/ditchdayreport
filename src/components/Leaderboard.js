import "./Leaderboard.css";

function Leaderboard() {
  return (
    <div className="leaderboard-section">
      <div className="main-title">Top 5 Leaderboard</div>
      <table>
        <tr>
          <th>Name</th>
          <th>Number of Reports</th>
          <th>Most recent comment</th>
        </tr>
        <tr>
          <td className="name">Andy Tong</td>
          <td className="number">375</td>
          <td className="comment">
            He’s literally boosted out of his mind He’s literally boosted out of
            his mind He’s literally boosted out of his mind He’s literally
            boosted out of his mind
          </td>
        </tr>
        <tr>
          <td className="name">Steve Guo</td>
          <td className="number">280</td>
          <td className="comment">
            {" "}
            Failed to get out of diamond after 7 years
          </td>
        </tr>
        <tr>
          <td className="name">Rachel Lin</td>
          <td className="number">152</td>
          <td className="comment">She’s a literal tomato guys let’s be real</td>
        </tr>
      </table>
    </div>
  );
}
export default Leaderboard;
