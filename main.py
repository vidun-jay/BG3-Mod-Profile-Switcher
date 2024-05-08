import os
import shutil
import glob
import inquirer
import time

# Function to get configuration settings from a hidden file or prompt the user
def get_configuration():
    config_file = os.path.join(os.path.expanduser('~'), '.bg3config')
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            lines = file.read().splitlines()
        mods_folder = lines[0]
        mod_manager_path = lines[1]
        return mods_folder, mod_manager_path
    else:
        mods_folder = input("Enter the location of the Mods folder: ")
        mod_manager_path = input("Enter the full path to BG3ModManager.exe: ")
        with open(config_file, 'w') as file:
            file.write(mods_folder + '\n' + mod_manager_path)
        return mods_folder, mod_manager_path

# Function to list all profiles from zip files with '-Mods' suffix
def list_profiles(mods_folder):
    os.chdir(mods_folder)
    zip_files = glob.glob('*-Mods.zip')
    profiles = [zip_file.split('-Mods.zip')[0] for zip_file in zip_files]
    return profiles

# Function to prompt user to select a profile
def select_profile(profiles):
    questions = [
        inquirer.List('profile',
                      message="Select a profile to set",
                      choices=profiles)
    ]
    answers = inquirer.prompt(questions)
    return answers['profile']

# Function to extract the selected zip file
def extract_zip_file(profile, mods_folder):
    zip_file = os.path.join(mods_folder, f"{profile}-Mods.zip")
    target_folder = os.path.join(mods_folder, 'Mods')
    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)
    os.makedirs(target_folder)
    shutil.unpack_archive(zip_file, target_folder)
    print("\033[92mProfile set successfully.\033[0m")
    time.sleep(3)


def main():
    mods_folder, mod_manager_path = get_configuration()
    profiles = list_profiles(mods_folder)
    if profiles:
        profile = select_profile(profiles)
        print("Setting profile, please wait...")
        extract_zip_file(profile, mods_folder)
    else:
        print("No mod profiles found.")

if __name__ == '__main__':
    main()
