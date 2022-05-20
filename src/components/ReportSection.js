import "./ReportSection.css";
import { useState, useEffect } from "react";
import axios from "axios";

async function populateDropdown() {
  let data = await fetch("/api/users");
  data = await data.json();
  for (let i = 0; i < data.length; i++) {
    let opt = document.createElement("option");
    opt.value = data[i].first_name + " " + data[i].last_name;
    opt.textContent = opt.value;
    document.querySelector(".report-dropdown").appendChild(opt);
  }
}

async function populateLeaderboard() {
  let data = await fetch("/api/reports");
  data = await data.json();
  let reports = {};
  for (let i = 0; i < data.length; i++) {
    let user_id = data[i].user;
    if (user_id in reports) {
      reports[user_id].push(data[i]);
    } else {
      reports[user_id] = [data[i]];
    }
  }

  let report_counts = [];
  for (const [key, value] of Object.entries(reports)) {
    report_counts.push({ user_id: key, report_count: value.length });
  }

  report_counts.sort(function (x, y) {
    if (x["report_count"] == y["report_count"]) return 0;
    else if (parseInt(x["report_count"]) < parseInt(y["report_count"]))
      return 1;
    else return -1;
  });

  let table = document.querySelector("table");

  for (let i = 0; i < Math.min(report_counts.length, 5); i++) {
    let name = await fetch("/api/users/" + report_counts[i].user_id);
    name = await name.json();
    report_counts[i]["name"] = name["first_name"] + " " + name["last_name"];
  }

  for (let i = 0; i < Math.min(report_counts.length, 5); i++) {
    document.getElementById("name-" + (i + 1)).textContent =
      report_counts[i].name;
    document.getElementById("number-" + (i + 1)).textContent =
      report_counts[i].report_count;

    let reports_on_this_user = reports[report_counts[i].user_id];
    document.getElementById("comment-" + (i + 1)).textContent =
      reports_on_this_user[reports_on_this_user.length - 1].report_text;
  }
}

function ReportSection() {
  const [numReports, setNumReports] = useState(0);
  const [lastReported, setLastReported] = useState("No reports yet");
  useEffect(() => {
    populateDropdown();
    setInterval(populateLeaderboard, 300);
  }, []);

  async function executeReport() {
    const player = document.querySelector(".report-dropdown").value;
    const is_negative_attitude =
      document.querySelector("#negative-attitude").checked;
    const is_trolling = document.querySelector("#trolling").checked;
    const is_verbal_abuse = document.querySelector("#verbal-abuse").checked;
    const is_unskilled_player =
      document.querySelector("#unskilled-player").checked;
    const is_is_andy_tong = document.querySelector("#is-andy-tong").checked;
    const report_reason = document.querySelector("textarea").value;
    let data = {
      player: player,
      is_negative_attitude: is_negative_attitude,
      is_trolling: is_trolling,
      is_verbal_abuse: is_verbal_abuse,
      is_unskilled_player: is_unskilled_player,
      is_is_andy_tong: is_is_andy_tong,
      report_reason: report_reason,
    };
    let response = await axios.post("/api/reports", data);
    setNumReports((prev) => {
      return prev + 1;
    });
    setLastReported(player);
  }

  return (
    <div className="report-section">
      <div className="report-box">
        <div className="report-header">
          <select className="report-dropdown">
            <option value="" disabled selected hidden>
              Choose player to report
            </option>
          </select>
          <div className="report-instructions">
            As inaccurately as you can, please tell us what happened with this
            player. Smash the report button as many times to report them
            multiple times ;)
          </div>
        </div>

        <div className="report-option">
          <input
            type="checkbox"
            id="negative-attitude"
            name="negative-attitude"
          />
          <div className="report-option-text">
            <div className="report-option-title">NEGATIVE ATTITUDE</div>
            <div className="report-option-description">
              This dude legit repels electrons that’s how negative s/he is
            </div>
          </div>
        </div>
        <div className="report-option">
          <input type="checkbox" id="trolling" name="trolling" />
          <div className="report-option-text">
            <div className="report-option-title">TROLLING</div>
            <div className="report-option-description">
              Straight running it down
            </div>
          </div>
        </div>
        <div className="report-option">
          <input type="checkbox" id="verbal-abuse" name="verbal-abuse" />
          <div className="report-option-text">
            <div className="report-option-title">VERBAL ABUSE</div>
            <div className="report-option-description">
              When you ask them to talk dirty to you but they start roasting
              your GPA :(
            </div>
          </div>
        </div>
        <div className="report-option">
          <input
            type="checkbox"
            id="unskilled-player"
            name="unskilled-player"
          />
          <div className="report-option-text">
            <div className="report-option-title">UNSKILLED PLAYER</div>
            <div className="report-option-description">
              My great grandma could 1v1 this person any day of the week.
            </div>
          </div>
        </div>
        <div className="report-option">
          <input type="checkbox" id="is-andy-tong" name="is-andy-tong" />
          <div className="report-option-text">
            <div className="report-option-title">IS ANDY TONG</div>
            <div className="report-option-description">
              Pretty self-explanatory, more or less a mix of everything above.
            </div>
          </div>
        </div>
        <textarea
          id="report-reason"
          name="report-reason"
          rows="4"
          className="report-reason"
          placeholder="Reason for report..."
        ></textarea>
        <button className="report-button" onClick={executeReport}>
          REPORT
        </button>
        <div className="num-reports">Reports submitted: {numReports}</div>
        <div className="last-reported">Last Reported: {lastReported}</div>
      </div>
    </div>
  );
}
export default ReportSection;
