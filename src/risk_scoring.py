def score_events(df):
    """
    Assigns a risk score:
      - Base score: 10 for normal events.
      - Add 40 points if a policy violation is detected.
      - For file transfers, add an additional 10 points if file_size > 10MB.
    """
    scores = []
    for idx, row in df.iterrows():
        score = 10
        if row["policy_violation"]:
            score += 40
            if row["activity_type"] == "file-transfer" and row["file_size"] != "NA":
                try:
                    size = int(row["file_size"].replace("MB", ""))
                    if size > 10:
                        score += 10
                except Exception:
                    pass
        scores.append(score)
    df["risk_score"] = scores
    return df

if __name__ == '__main__':
    import pandas as pd
    from data_generator import generate_dlp_events
    from dlp_policy_mapper import map_dlp_policies
    df_sample = generate_dlp_events(10)
    mapped = map_dlp_policies(df_sample)
    scored = score_events(mapped)
    print(scored[["event_id", "risk_score"]])
