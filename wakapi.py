""" A simple script to import backlogged data from wakatime > wakapi backends."""
import hashlib
import random
import time
from datetime import datetime, timedelta

import requests

# Configuration dictionary
config = {
    "wakatime": {
        "url": "https://wakatime.com/api/v1/users/current/heartbeats?date={date}",
        "cookie_name": "session",
        "cookie_value": "PLEASE ENTER YOUR SESSION HERE", # it's the session cookie when you're logged in 
    },
    "wakapi": {
        "url": "https://{PLEASE_CHANGE_TO_YOUR_WAKAPI_INSTANCE}/api/v1/users/current/heartbeats.bulk",
        "cookie_name": "wakapi_auth",
        "cookie_value": "", # wakapi_auth cookie
    },
    "time_range": {
        "days": 100,  # Number of days to go back
        "start_date": "2024-11-23",  # Specify the start date
    },
    "delay": {
        "min": 1,  # Minimum delay in seconds
        "max": 3,  # Maximum delay in seconds
    },
    "log": {"file": "hashes.log"},
}


# Function to generate a hash for the response data
def generate_hash(data):
    return hashlib.sha256(str(data).encode("utf-8")).hexdigest()


# Function to check if a hash exists in the log file
def is_hash_processed(hash_value):
    try:
        with open(config["log"]["file"], "r") as log_file:
            for line in log_file:
                if hash_value in line:
                    return True
    except FileNotFoundError:
        pass  # Log file doesn't exist yet
    return False


# Function to log a hash and date
def log_hash(hash_value, date):
    with open(config["log"]["file"], "a") as log_file:
        log_file.write(f"{hash_value} {date}\n")


# Parse start_date from config
start_date_str = config["time_range"]["start_date"]
try:
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
except ValueError:
    print("Invalid start_date format. Please use 'YYYY-MM-DD'.")
    exit()

# Calculate end_date by subtracting the number of days from start_date
end_date = start_date - timedelta(days=config["time_range"]["days"])

# Process each date from start_date backwards to end_date
current_date = start_date
while current_date >= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    wakatime_url = config["wakatime"]["url"].format(date=date_str)
    wakatime_headers = {
        "Cookie": f"{config['wakatime']['cookie_name']}={config['wakatime']['cookie_value']}"
    }

    try:
        # Fetch heartbeats from Wakatime
        response = requests.get(wakatime_url, headers=wakatime_headers)
        response.raise_for_status()
        data = response.json()
        heartbeats = data.get("data", [])

        if heartbeats:
            # Generate hash for the response data
            hash_value = generate_hash(heartbeats)

            # Check if the hash has already been processed
            if is_hash_processed(hash_value):
                print(f"Data for {date_str} has already been processed. Skipping.")
            else:
                # Send heartbeats to Wakapi
                wakapi_headers = {
                    "Cookie": f"{config['wakapi']['cookie_name']}={config['wakapi']['cookie_value']}",
                    "Content-Type": "application/json",
                }
                wakapi_response = requests.post(
                    config["wakapi"]["url"], headers=wakapi_headers, json=heartbeats
                )
                wakapi_response.raise_for_status()
                print(
                    f"Successfully posted heartbeats for {date_str}. Response: {wakapi_response.status_code} {wakapi_response.text}"
                )

                # Log the hash and date
                log_hash(hash_value, date_str)
        else:
            print(f"No heartbeats for {date_str}")

        # Introduce random delay
        delay = random.uniform(config["delay"]["min"], config["delay"]["max"])
        time.sleep(delay)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred for {date_str}: {http_err}")
    except Exception as err:
        print(f"An error occurred for {date_str}: {err}")

    current_date -= timedelta(days=1)

# Print the calculated end_date and exit
print(
    f"Processed dates from {start_date_str} to {end_date.strftime('%Y-%m-%d')}. Exiting."
)
