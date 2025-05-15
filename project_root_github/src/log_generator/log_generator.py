
import random
from datetime import datetime, timedelta

class LogGenerator:
    def __init__(self):
        self.severities = ['ERROR', 'WARNING', 'INFO']
        self.start_time = datetime.now()

    def generate_log_entry(self, index):
        time_offset = timedelta(seconds=random.randint(0, 86400))
        timestamp = self.start_time + time_offset
        severity = random.choice(self.severities)
        return f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} [{severity}] Log {index} message"

    def generate_log_file(self, filename, total_entries):
        with open(filename, 'w') as f:
            for i in range(total_entries):
                f.write(self.generate_log_entry(i) + '\n')
