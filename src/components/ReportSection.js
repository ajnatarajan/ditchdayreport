import "./ReportSection.css";

function ReportSection() {
  return (
    <div className="report-section">
      <div className="report-box">
        <div className="report-header">
          <select className="report-dropdown">
            <option value="" disabled selected hidden>
              Choose player to report
            </option>
            <option value="Steve">Steve Guo</option>
            <option value="Steve">Steve Guo</option>
            <option value="Steve">Steve Guo</option>
            <option value="Steve">Steve Guo</option>
            <option value="Steve">Steve Guo</option>
            <option value="Steve">Steve Guo</option>
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
        <button className="report-button">REPORT</button>
      </div>
    </div>
  );
}
export default ReportSection;
