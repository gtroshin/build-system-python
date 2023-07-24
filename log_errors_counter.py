import argparse
import os
from collections import defaultdict

"""
It parses log files in the logs directory and counts unique errors per user in a given date range

Args:
    start_week (int): The start of the date range (week number)
    end_week (int): The end of the date range (week number).
    log_dir (str): The directory where the log files are located.

Returns:
    Prints the results of unique error counts per user
"""
def parse_logs(start_week, end_week, log_dir):
    if not os.path.exists(log_dir):
        raise FileNotFoundError(f"{log_dir} directory not found!")

    # Dict to store unique error counts per user
    error_counts = defaultdict(lambda: defaultdict(set))

    # Iterate over log files in the logs directory
    log_files = [filename for filename in os.listdir(log_dir) if '-' in filename and '.' in filename]
    if not log_files:
        raise FileNotFoundError(f"No log files found in {log_dir} directory!")
    for filename in log_files:
        week_number = int(filename.split('-')[1].split('.')[0])
        if start_week <= week_number <= end_week:
            with open(os.path.join(log_dir, filename), 'r') as file:
                if "access" in filename:
                    # Parse access log
                    for line in file:
                        transaction_id, datestamp, status_code, user, _ = line.strip().split()
                        if int(status_code) == -1:
                            error_counts[user]["access"].add(transaction_id)
                else:
                    # Parse error log
                    transaction_id = None
                    for line in file:
                        if line.startswith('['):
                            transaction_id = line.strip()[1:-1]
                        else:
                            error_message = line.strip()
                            error_counts[transaction_id]["error"].add(error_message)

    for user, error_types in error_counts.items():
        for error_type, errors in error_types.items():
            print(f"User: {user}, Error Type: {error_type}, Unique Errors: {len(errors)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count unique errors per user in a given date range")

    parser.add_argument("start_week", type=int, help="Start of the date range (week number)")
    parser.add_argument("end_week", type=int, help="End of the date range (week number)")
    parser.add_argument("log_dir", type=str, nargs='?', default='logs', help="Directory where the log files are located")
    
    args = parser.parse_args()

    parse_logs(args.start_week, args.end_week, args.log_dir)
