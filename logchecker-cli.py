#!/usr/bin/env python3
"""Check RIP log score using the Redacted API."""

import time
import json
import sys
import os
import chardet
import requests

URL = 'https://redacted.sh/ajax.php?action=logchecker'

def main():
    """Run the log checker script."""
    # Retrieve API key from environment variable
    try:
        api_key = os.getenv('RED_API_KEY')
        if not api_key:
            print("Please set the $RED_API_KEY environment variable as your API key!")
            sys.exit(1)

        # Check command-line arguments
        if len(sys.argv) < 2:
            print("Usage: logchecker [FILE] [--all]")
            sys.exit(1)

        if sys.argv[1] == '--all':
            # Traverse directories for .log files
            log_files = []
            for dirpath, _, filenames in os.walk('.'):
                for filename in filenames:
                    if filename.lower().endswith('.log'):
                        log_files.append(os.path.join(dirpath, filename))

            if not log_files:
                print("No .log files found!")
                sys.exit(1)

            for log_path in log_files:
                process_log_file(log_path, api_key)
                time.sleep(2)  # Delay between processing files

        else:
            # Get log file path from command-line arguments
            log_path = sys.argv[1]
            process_log_file(log_path, api_key)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Aborting...")
        sys.exit(0)

def process_log_file(log_path, api_key):
    """Process a single log file."""
    print(f"Processing {log_path}...")

    # Convert relative path to absolute path
    log_path = os.path.abspath(log_path)

    # Check if file has a .log extension
    if not log_path.lower().endswith('.log'):
        print("Not a log file! Please provide a valid .log file.")
        sys.exit(1)

    # Detect file encoding
    try:
        with open(log_path, 'rb') as f:
            raw_data = f.read()
            encoding = chardet.detect(raw_data)['encoding']
    except (FileNotFoundError, IOError) as e:
        print(f"Error opening file: {e}")
        return  # Skip to the next file

    # Open the file for reading
    try:
        with open(log_path, 'r', encoding=encoding, errors='ignore') as f:
            logfile = {'log': f}
            headers = {'Authorization': api_key}
            response = requests.post(URL, headers=headers, files=logfile, timeout=5)
            response.raise_for_status()  # Check for HTTP errors

            # Parse and display the response
            data = response.json()
            score = data['response']['score']
            print(f"Score: {score}")
            if score == 100:
                print("Perfect Score! No Issues reported.")
            else:
                print("Issues:")
                for item in data['response']['issues']:
                    print(item)
    except requests.RequestException as e:
        print(f"Error making POST request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
