# BG3 Mod Manager Script
This Python script facilitates managing mods for Baldur's Gate 3. It allows users to select a mod profile from .zip files located in a specified Mods folder and automatically extracts the selected profile to a designated directory. The script saves user settings to streamline future operations.

## Features
- Automatically detects and lists mod profiles from .zip files.
- Extracts and sets up the selected mod profile in the "Mods" folder.
- Saves the Mods folder and BG3ModManager executable path for future use.

## Prerequisites
- Python 3.12.3 installed on your system
- inquirer Python library (for user-friendly CLI interactions)
## Installation
Clone this repository or download the script directly.
Install the required Python packages:
```bash
pip install inquirer
```
## Usage
Run the script from the command line:

```bash
python bg3_mod_manager.py
```
On the first run, you will be prompted to enter the path to your Mods folder and the full path to the BG3ModManager.exe. These paths will be saved and used for subsequent executions.

Configuration
The script saves the configurations in a hidden file named `.bg3config` in the user's home directory. This file includes:

- The path to the Mods folder.
- The path to the BG3ModManager.exe.
