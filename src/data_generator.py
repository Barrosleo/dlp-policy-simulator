import pandas as pd
import random
import datetime

def generate_dlp_events(num_records=100):
    users = ['alice', 'bob', 'charlie', 'dave']
    activity_types = ['file-transfer', 'file-access', 'login']
    file_names = ['confidential_report.pdf', 'employee_data.xlsx', 'internal_memo.docx',
                  'classified_strategy.pdf', 'public_presentation.pptx']
    actions = {
        'file-transfer': ['download', 'upload'],
        'file-access': ['view', 'edit'],
        'login': ['login-success', 'login-failure']
    }
    
    events = []
    for i in range(num_records):
        activity = random.choice(activity_types)
        event = {
            "event_id": i+1,
            "timestamp": datetime.datetime.now().isoformat(),
            "user": random.choice(users),
            "activity_type": activity,
            "file_name": random.choice(file_names) if activity != 'login' else "NA",
            "file_size": f"{random.randint(1, 30)}MB" if activity != 'login' else "NA",
            "action": random.choice(actions[activity])
        }
        events.append(event)
    return pd.DataFrame(events)

if __name__ == '__main__':
    df = generate_dlp_events(10)
    print(df.head())
