# BG3 Mod Manager Script
This Python script facilitates managing mods for Baldur's Gate 3. It allows users to select a mod profile from .zip files located in a specified Mods folder and automatically extracts the selected profile to a designated directory. The script saves user settings to streamline future operations.

## Features
- Automatically detects and lists mod profiles from .zip files.
- Extracts and sets up the selected mod profile in the "Mods" folder.
- Saves the Mods folder and BG3ModManager executable path for future use.

## Installation
  1. Navigate to the GitHub repository's [releases](https://github.com/vidun-jay/BG3-Mod-Profile-Switcher/releases/tag/v0.1.0) page.
2. Download the latest `Setup.exe` file for the BG3 Mod Manager.
3. Run the downloaded `Setup.exe` to install the mod manager on your system.

## Usage
1. Open the BG3 Mod Manager from your desktop shortcut or from the Start Menu.
2. On the first run, you will be prompted to enter the path to your Mods folder and the full path to BG3ModManager.exe. These paths will be saved in `.bg3config` for subsequent uses.
3. The script will list all available mod profiles based on the zipped files in the Mods folder. Select a profile to set it up for your game.

⚠️**Note:** For each profile, zip the files and name it `<profile-name>-Mods.zip`. This is important as the script looks for the "`*-Mods`" suffix.

Configuration
The script saves the configurations in a hidden file named `.bg3config` in the user's home directory. This file includes:

- The path to the Mods folder.
- The path to the BG3ModManager.exe.
