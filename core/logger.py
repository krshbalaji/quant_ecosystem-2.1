import os
import json
import datetime


class SystemLogger:
    def __init__(self):
        today = datetime.date.today().isoformat()
        self.log_dir = "logs"
        self.file_path = os.path.join(self.log_dir, f"{today}_session_log.json")

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def log_cycle(self, data):
        timestamp = datetime.datetime.now().isoformat()

        entry = {
            "timestamp": timestamp,
            **data
        }

        with open(self.file_path, "r") as f:
            logs = json.load(f)

        logs.append(entry)

        with open(self.file_path, "w") as f:
            json.dump(logs, f, indent=4)