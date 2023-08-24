# This is a script to check the connection of the network on this device every 5 minutes.
from ping3 import ping, verbose_ping
import yaml
import os
import time

# X seconds to repeat to check the connection of the network
time_to_repeat = 300
host = "8.8.8.8"


def check_connection():
    response_time = ping(host)
    if response_time is False:
        result = {
            "Time": time.ctime(),
            "Connection": "Failed",
            "Response time": 0
        }
    else:
        response_time_in_ms = "{:.0f}".format(response_time * 1000)
        result = {
            "Time": time.ctime(),
            "Connection": "Succeeded",
            "Response time": f"{response_time_in_ms}ms"
        }
    saveResult(result)


def saveResult(result):
    user_home = os.path.expanduser("~")
    yaml_path = os.path.join(user_home, 'network-connection.yaml')
    try:
        with open(yaml_path, "r") as yaml_file:
            existing_results = yaml.safe_load(yaml_file)
    except FileNotFoundError:
        existing_results = []
    existing_results.append(result)
    with open(yaml_path, "w") as yaml_file:
        yaml.dump(existing_results, yaml_file)
    print(f"YAML file saved at: {yaml_path}")

while(True):
    for i in range(4):
        check_connection()
        print(ping(host))
    time.sleep(time_to_repeat)