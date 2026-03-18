# System Details

System Details is a desktop application written in Python with PySide6 for viewing Linux system information in a graphical interface. The app brings together useful machine details such as operating system information, CPU data, disk usage, user details, kernel information, network data, and hardware sensor readings in one place.

## Features

- View operating system information
- Display CPU and hardware details
- Show disk usage and storage information
- Display user and group details
- Read kernel-related information
- Show network-related details
- Display sensor and temperature data
- Simple desktop interface built with Qt
- Python dependencies managed with `requirements.txt`

## Technologies Used

- Python
- PySide6
- Linux system files and commands
- Python packages listed in `requirements.txt`

## Requirements

Before running the application, make sure you have:

- Python 3.10 or newer
- `pip`
- A Linux system for full compatibility

Some features may depend on standard Linux files or commands such as:

- `/etc/os-release`
- `/proc/modules`
- `df`
- `id`
- `whoami`
- `lscpu`
- `lsblk`
- `sensors`
- `ip`

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/system-details.git
cd system-details
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python sysdetails.py