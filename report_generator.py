import pandas as pd
from db import collection
import os

def generate_daily_report(date_str):
    records = list(collection.find({"date": date_str}, {"_id": 0}))
    if not records:
        print(f"No records found for {date_str}")
        return None

    df = pd.DataFrame(records)

    # ✅ Corrected columns
    print(f"\n📅 Report for {date_str}")
    print(df[["emp_id", "name", "login_time", "logout_time", "hours_worked"]])

    # Ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    report_path = f"reports/{date_str}_report.csv"
    df.to_csv(report_path, index=False)
    return report_path