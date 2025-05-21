
import random
from datetime import datetime, timedelta

class LogGenerator:
    def __init__(self):
        self.severities = ['ERROR', 'WARNING', 'INFO']
        self.start_time = datetime.now()

    def generate_log_entry(self, timestamp, index):
        severity = random.choice(self.severities)
        message = f"Log entry {index}: Sample message content"
        return f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} [{severity}] {message}"

    def generate_logs(self, total_entries, pattern='random'):
        logs = []
        base_time = self.start_time
        for i in range(total_entries):
            offset = timedelta(seconds=random.randint(0, 86400))
            timestamp = base_time + offset
            logs.append(self.generate_log_entry(timestamp, i))

        if pattern == 'sorted':
            logs.sort()
        elif pattern == 'reverse':
            logs.sort(reverse=True)
        elif pattern == 'partial':
            logs[:int(0.7 * len(logs))] = sorted(logs[:int(0.7 * len(logs))])
            random.shuffle(logs[int(0.7 * len(logs)):])
        return logs

    def generate_log_file(self, filename, total_entries, pattern='random'):
        logs = self.generate_logs(total_entries, pattern)
        with open(filename, 'w') as f:
            f.writelines(line + '\n' for line in logs)
