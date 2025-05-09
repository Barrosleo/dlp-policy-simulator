def trigger_alerts(df, threshold=50):
    """
    For each event with a risk_score equal to or above a threshold, simulate sending an alert.
    Returns a list of alert messages.
    """
    alerts = []
    for idx, row in df.iterrows():
        if row.get("risk_score", 0) >= threshold:
            alert_msg = (f"ALERT: Event {row['event_id']} by {row['user']} "
                         f"has a risk score of {row['risk_score']}. Review required.")
            alerts.append(alert_msg)
    return alerts

if __name__ == '__main__':
    from risk_scoring import score_events
    from data_generator import generate_dlp_events
    from dlp_policy_mapper import map_dlp_policies
    import pandas as pd
    df_sample = generate_dlp_events(10)
    mapped = map_dlp_policies(df_sample)
    scored = score_events(mapped)
    alerts = trigger_alerts(scored)
    print(alerts)
