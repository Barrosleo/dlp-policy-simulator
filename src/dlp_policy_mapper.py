def map_dlp_policies(df):
    """
    Evaluates simulated DLP events against policy rules.
      - File transfers involving files with 'confidential' or 'classified' in the name and file_size > 10MB are marked as violations.
      - Any login-failure events are flagged as potential risks.
    """
    df["policy_violation"] = False
    df["violation_reason"] = ""
    
    for idx, row in df.iterrows():
        if row["activity_type"] == "file-transfer" and row["file_name"] != "NA":
            if any(keyword in row["file_name"].lower() for keyword in ["confidential", "classified"]):
                try:
                    size = int(row["file_size"].replace("MB", ""))
                    if size > 10:
                        df.at[idx, "policy_violation"] = True
                        df.at[idx, "violation_reason"] = "large sensitive file transfer"
                except:
                    pass
        if row["activity_type"] == "login" and row["action"] == "login-failure":
            df.at[idx, "policy_violation"] = True
            df.at[idx, "violation_reason"] = "failed login"
    return df

if __name__ == '__main__':
    import pandas as pd
    from data_generator import generate_dlp_events
    df_sample = generate_dlp_events(10)
    mapped = map_dlp_policies(df_sample)
    print(mapped[["event_id", "file_name", "policy_violation", "violation_reason"]])
