#!/usr/bin/env python3
"""Check RIP log score using the Redacted API."""

import json
import sys
import os
import requests
import chardet

def main():
    """Run the log checker script."""
    # Retrieve API key from environment variable
    api_key = os.getenv('RED_API_KEY')
    if not api_key:
        print("Please set the $RED_API_KEY environment variable as your API key!")
        sys.exit(1)

    # Get log file path from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: logchecker [FILE]")
        sys.exit(1)

    log_path = sys.argv[1]

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
        sys.exit(1)

    # Open the file for reading
    try:
        with open(log_path, 'r', encoding=encoding, errors='ignore') as f:
            logfile = {'log': f}
            headers = {'Authorization': api_key}
            url = 'https://redacted.ch/ajax.php?action=logchecker'
            response = requests.post(url, headers=headers, files=logfile, timeout=5)
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
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
