from data_generator import generate_dlp_events
from dlp_policy_mapper import map_dlp_policies
from risk_scoring import score_events
from alert_system import trigger_alerts
from report_generator import generate_report
import os

def main():
    # Ensure necessary directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)
    
    # Generate synthetic DLP events and save to CSV
    df_events = generate_dlp_events(200)
    df_events.to_csv("data/simulated_dlp_events.csv", index=False)
    print("Synthetic DLP events generated.")
    
    # Map events against DLP policies to detect violations
    mapped_events = map_dlp_policies(df_events)
    print("DLP policy mapping complete.")
    
    # Calculate risk scores for each event
    scored_events = score_events(mapped_events)
    print("Risk scoring complete.")
    
    # Trigger automated alerts for high-risk incidents
    alerts = trigger_alerts(scored_events)
    print("Automated alerts triggered:", alerts)
    
    # Generate the incident report and save it
    report = generate_report(scored_events)
    with open("docs/incident_report.json", "w") as f:
        f.write(report)
    print("Incident report generated at docs/incident_report.json")

if __name__ == '__main__':
    main()
