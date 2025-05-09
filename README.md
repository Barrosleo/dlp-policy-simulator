# dlp policy simulator

This project simulates potential data exfiltration and leakage scenarios by generating synthetic DLP events, mapping these events against predefined DLP policies, calculating risk scores, triggering automated alerts for high-risk incidents, and generating comprehensive incident reports with remediation recommendations.

## Key Features
- **Synthetic Data Generation:** Simulate file transfers, data downloads, and unauthorized access attempts.
- **DLP Policy Mapping:** Evaluate simulated events against established DLP rules to flag control gaps.
- **Risk Scoring:** Calculate risk scores based on event severity and data loss impact.
- **Automated Alerting:** Simulate notifications for events that exceed a risk threshold.
- **Reporting:** Generate detailed incident reports with analysis and recommendations for policy updates.

## Usage
1. Open the project in GitHub Codespaces or use the web editor.
2. Install dependencies with:
pip install -r requirements.txt

3. Run the simulator:
python src/main.py

## Repository Structure
dlp-policy-simulator/
├── README.md
├── requirements.txt
├── docs/
│   └── incident_report.json
├── data/
│   └── simulated_dlp_events.csv
└── src/
    ├── main.py
    ├── data_generator.py
    ├── dlp_policy_mapper.py
    ├── risk_scoring.py
    ├── alert_system.py
    └── report_generator.py

