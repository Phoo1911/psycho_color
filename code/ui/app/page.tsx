// app/page.js
'use client'; // 클라이언트 사이드 스크립트(app.js)가 필요하면 선언

export default function Page() {
  return (
    <div className="container">
      <header className="text-center my-5">
        <h1 className="display-4">Psycho-Color Analysis System</h1>
        <p className="lead">
          Discover your personality traits through color preferences
        </p>
      </header>

      <div className="row">
        <div className="col-md-8 offset-md-2">
          {/* --- Color Preference Form (기존 index.html 폼) --- */}
          <div className="card mb-5">
            <div className="card-header bg-primary text-white">
              <h2 className="h4 mb-0">Color Preference Assessment</h2>
            </div>
            <div className="card-body">
              <form id="colorPreferenceForm">
                {/* 1. Color Ranking */}
                <div className="mb-4">
                  <h3 className="h5">1. Color Ranking</h3>
                  <p>
                    Drag and drop the colors to rank them from most
                    preferred (top) to least preferred (bottom).
                  </p>
                  <ul
                    id="colorRanking"
                    className="list-group color-ranking"
                  >
                    {[
                      'red',
                      'blue',
                      'green',
                      'yellow',
                      'purple',
                      'orange',
                      'pink',
                      'black',
                      'white',
                      'brown',
                    ].map((c) => (
                      <li
                        key={c}
                        className="list-group-item"
                        data-color={c}
                        style={{
                          backgroundColor:
                            {
                              red: '#e74c3c',
                              blue: '#3498db',
                              green: '#2ecc71',
                              yellow: '#f1c40f',
                              purple: '#9b59b6',
                              orange: '#e67e22',
                              pink: '#fd79a8',
                              black: '#2c3e50',
                              white: '#ecf0f1',
                              brown: '#795548',
                            }[c],
                          color:
                            c === 'black' || c === 'brown'
                              ? 'white'
                              : 'inherit',
                        }}
                      >
                        {c.charAt(0).toUpperCase() + c.slice(1)}
                      </li>
                    ))}
                  </ul>
                </div>
                {/* 이하 Contextual Preferences, Color–Emotion 부분도 동일하게 JSX로 옮깁니다. */}
                <div className="text-center">
                  <button
                    type="submit"
                    className="btn btn-primary btn-lg"
                  >
                    Generate Psychological Profile
                  </button>
                </div>
              </form>
            </div>
          </div>

          {/* --- Results Section --- */}
          <div
            id="resultsSection"
            className="card mb-5 d-none"
          >
            <div className="card-header bg-success text-white">
              <h2 className="h4 mb-0">Your Psychological Profile</h2>
            </div>
            <div className="card-body">
              {/* Jung Color Energy, Personality Overview, Charts, Recommendations */}
              {/* ... */}
              <div className="text-center">
                <button
                  id="startOverBtn"
                  className="btn btn-secondary btn-lg me-2"
                >
                  Start Over
                </button>
                <button
                  id="downloadReportBtn"
                  className="btn btn-primary btn-lg"
                >
                  Download Full Report
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <footer className="text-center my-5">
        <p>Psycho-Color Analysis System © 2025</p>
      </footer>
    </div>
  );
}
