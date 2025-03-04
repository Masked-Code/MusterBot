import os
import time
import pyautogui
import schedule
import random
from datetime import datetime, timedelta

def open_slack():
    """Opens the Slack desktop application."""
    if os.name == "nt": 
        os.system("start slack")
    elif os.name == "posix":
        os.system("open -a Slack" if "darwin" in os.uname().sysname.lower() else "slack &")
    time.sleep(5) 

def navigate_to_muster():
    """Searches and opens the 'muster' channel."""
    pyautogui.hotkey("ctrl", "k")
    time.sleep(1)
    pyautogui.write("muster", interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)

def send_message():
    """Sends 'In by 0800' in the channel."""
    pyautogui.write("In by 0800", interval=0.1)
    pyautogui.press("enter")

def automate_slack_message():
    """Automates the entire process with a random delay."""
    delay = random.randint(1, 10) * 60
    print(f"Delaying message by {delay // 60} minutes...")
    time.sleep(delay)
    open_slack()
    navigate_to_muster()
    send_message()
    print(f"Message sent at {datetime.now()}")

def schedule_randomized_message(day, base_time="06:30"):
    """Schedules a message with a randomized delay within a 1-10 min range."""
    hour, minute = map(int, base_time.split(":"))
    base_datetime = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
    random_delay = timedelta(minutes=random.randint(1, 10))
    scheduled_time = (base_datetime + random_delay).strftime("%H:%M")
    schedule.every().__getattribute__(day).at(scheduled_time).do(automate_slack_message)
    print(f"Scheduled message for {day.capitalize()} at {scheduled_time}")

schedule_randomized_message("monday")
schedule_randomized_message("tuesday")
schedule_randomized_message("wednesday")
schedule_randomized_message("thursday")
schedule_randomized_message("friday")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
