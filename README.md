# Digital Clock GUI

A clean and simple digital clock application built with Python and Tkinter.

The application displays the current time and date in a graphical interface and allows the user to switch between 12-hour and 24-hour time formats. The clock can also be paused and resumed whenever needed.

## Features

- Live digital clock
- Current date display
- 24-hour time format
- 12-hour time format with AM/PM
- 12-hour / 24-hour format toggle
- Pause and resume controls
- Automatic time updates every second
- Clean and simple graphical interface
- Class-based Python structure
- No external Python packages required

## Controls

| Control | Action |
|---|---|
| Switch to 12-hour | Changes the clock to 12-hour format |
| Switch to 24-hour | Changes the clock to 24-hour format |
| Pause | Stops the clock from updating |
| Resume | Starts the clock updating again |
| Window Close | Closes the application |

## Requirements

- Python 3.8 or later
- Tkinter

Tkinter is included with most standard Python installations.

## Installation

Clone the repository:

git clone https://github.com/RaavanHrishi07/Digital-Clock-GUI.git

Move into the project directory:

cd Digital-Clock-GUI

No additional Python packages are required.

## Run the Application

python main.py

## How It Works

The application uses Python's Tkinter library to create the graphical interface.

The current date and time are obtained using Python's datetime module.

The clock display is updated once every second using Tkinter's after() scheduling mechanism.

The application supports two time formats:

- 24-hour format: HH:MM:SS
- 12-hour format: HH:MM:SS AM/PM

The Pause button stops the scheduled clock update, while the Resume button starts it again.

## Project Structure

Digital-Clock-GUI/
├── main.py
├── README.md
├── .gitignore
└── LICENSE

## Technologies Used

- Python
- Tkinter
- datetime

## Author

Hrishikesh Sharma

GitHub: RaavanHrishi07

## License

This project is licensed under the MIT License. See the LICENSE file for details.