import json
from datetime import datetime

def generate_report(df):
    """
    Generates a JSON report summarizing:
      - Total events
      - Total policy violations
      - Average risk score
      - Details of high-risk events
      - Recommendations for policy updates
    """
    total_events = len(df)
    violations = df[df["policy_violation"]]
    total_violations = len(violations)
    avg_risk = df["risk_score"].mean() if total_events > 0 else 0
    high_risk_events = violations[violations["risk_score"] >= 50].to_dict(orient="records")
    
    recommendations = []
    if total_violations > 0:
        recommendations.append("Review file transfer policies and system login immunity.")
        recommendations.append("Implement stricter DLP controls for files exceeding sensitive thresholds.")
    
    report = {
        "report_generated": datetime.now().isoformat(),
        "total_events": total_events,
        "total_violations": total_violations,
        "average_risk_score": avg_risk,
        "high_risk_events": high_risk_events,
        "recommendations": recommendations
    }
    return json.dumps(report, indent=4)

if __name__ == '__main__':
    import pandas as pd
    from data_generator import generate_dlp_events
    from dlp_policy_mapper import map_dlp_policies
    from risk_scoring import score_events
    df_sample = generate_dlp_events(10)
    mapped = map_dlp_policies(df_sample)
    scored = score_events(mapped)
    report = generate_report(scored)
    print(report)
