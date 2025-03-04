# Automated Slack Message Bot

## Overview

- This Python script automates sending a message to a specific Slack channel (muster) every weekday morning at a randomized time between 06:31 and 06:40 AM. It opens the Slack desktop application, navigates to the channel, and types the message "In by 0800."

## Features

- Automatically opens the Slack desktop app

- Navigates to the "muster" channel

- Sends a predefined message

- Randomly delays the message by 1-10 minutes to avoid predictability

- Runs continuously in the background

## Prerequisites

### System Requirements

- Python 3.7 or later

- Slack desktop application installed

- A working internet connection

### Required Python Packages

- pyautogui

- schedule

## Setup Instructions

1. Clone the Repository

```
git clone https://github.com/yourusername/slack-bot.git
cd slack-bot
```

2. Create and Activate a Virtual Environment

- Windows (Command Prompt)

```
python -m venv venv
venv\Scripts\activate
```

- Mac/Linux

```
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```

## Usage

### Running the Script

- Once the setup is complete, run the script:

```
python main.py
```

- This will start the automation process, running in the background and sending the message at the scheduled time.

### Keeping the Script Running

- For continuous operation, consider running it in the background:

- On Linux/Mac:

```
nohup python slack_bot.py &
```

- On Windows (PowerShell):

```
Start-Process python -ArgumentList "slack_bot.py" -NoNewWindow
```

## Troubleshooting

1. Slack Doesn't Open

- Ensure Slack is installed and accessible via the command line.

- Try opening Slack manually and verify it launches correctly.

2. Dependencies Not Found

- Ensure the virtual environment is activated before running the script.

- Reinstall dependencies using:

```
pip install --upgrade -r requirements.txt
```

3. Script Doesn't Run at the Scheduled Time

- Check that the script is actively running.

- Verify system time settings to ensure correct scheduling.

- If necessary, manually adjust the random delay settings in the script.

## Customization

### Changing the Message

- Edit the send_message() function in slack_bot.py:

```python
pyautogui.write("Your custom message here", interval=0.1)
```

### Adjusting the Time

Modify the base time in schedule_randomized_message() function:

```python
schedule_randomized_message("monday", base_time="07:00")  # Change from 06:30 to 07:00
```