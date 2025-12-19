from datetime import datetime
from db import collection

def login(emp_id, name):
    active_session = collection.find_one({"emp_id": emp_id, "logout_time": None})
    if active_session:
        return False, f"Employee {name} (ID: {emp_id}) is already logged in."

    now = datetime.now()
    record = {
        "emp_id": emp_id,
        "name": name,
        "date": now.strftime("%Y-%m-%d"),
        "login_time": now.strftime("%H:%M:%S"),
        "logout_time": None,
        "hours_worked": None
    }
    collection.insert_one(record)
    return True, f"Login recorded for {name}."


def logout(emp_id):
    now = datetime.now()
    record = collection.find_one_and_update(
        {"emp_id": emp_id, "logout_time": None},
        {"$set": {"logout_time": now.strftime("%H:%M:%S")}},
        return_document=True
    )
    if record:
        try:
            login_time = datetime.strptime(record["login_time"], "%H:%M:%S")
            logout_time = datetime.strptime(now.strftime("%H:%M:%S"), "%H:%M:%S")
            hours = (logout_time - login_time).seconds / 3600
            collection.update_one(
                {"_id": record["_id"]},
                {"$set": {"hours_worked": round(hours, 2)}}
            )
        except Exception:
            pass
        return True, "Logout successful."
    else:
        return False, "No active login found."


def get_status(emp_id):
    active_session = collection.find_one({"emp_id": emp_id, "logout_time": None})
    if active_session:
        return True
    return False