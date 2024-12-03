# Mouse Mover

This Python application moves the mouse cursor 1 pixel in a random direction every minute and runs in the background until stopped.

## Requirements

- Python 3.x
- `pyautogui` library

## Installation

1. Download the `mouse_mover.py` file.
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

## Activate the virtual environment:

On Windows (using Git Bash):
```sh
source venv/Scripts/activate
```

On Mac:
```sh
source venv/bin/activate
```

## Install the required packages:
```sh
pip install pyautogui
```

## Usage
To run the script in the background:
```sh
nohup python mouse_mover.py &
```

This will start the script and run it in the background. The output will be redirected to a file named nohup.out.

## Stopping the Script
To stop the script, you need to find the process ID (PID) and kill it.

Kill the process using the PID:
```sh
kill <PID>
```
Replace <PID> with the actual process ID of the running script..

Shutdown virtual environment:
```sh
deactivate
```

## Windows task configuration

To have your Python script run automatically when Windows starts, you can create a scheduled task using the Task Scheduler. Here are the steps:

Create a batch file to run the script: Create a batch file (e.g., run_mouse_mover.bat) with the following content:

```
@echo off
cd C:\path\to\your\project
call venv\Scripts\activate
python mouse_mover.py
```

Replace C:\path\to\your\project with the actual path to your project directory.

Open Task Scheduler: Press Win + R, type taskschd.msc, and press Enter to open Task Scheduler.

Create a new task:

In the Task Scheduler window, click on "Create Task" in the right-hand pane.
In the "General" tab, provide a name for the task (e.g., "Mouse Mover").
Optionally, provide a description.
Set the trigger:

Go to the "Triggers" tab and click "New".
In the "New Trigger" window, select "At log on" from the "Begin the task" dropdown.
Click "OK".
Set the action:

Go to the "Actions" tab and click "New".
In the "New Action" window, select "Start a program" from the "Action" dropdown.
Click "Browse" and select the batch file you created (run_mouse_mover.bat).
Click "OK".
Configure additional settings (optional):

Go to the "Conditions" tab and configure any additional conditions if needed.
Go to the "Settings" tab and configure any additional settings if needed.
Save the task:

Click "OK" to save the task.
Now, your Python script will run automatically when you log on to Windows.