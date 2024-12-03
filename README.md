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