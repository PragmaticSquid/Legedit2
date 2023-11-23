#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess

dbg          = 0

def run_system_command(command):
    try:
        # Use subprocess.run() to execute the system command
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the command was successful (return code 0)
        if result.returncode == 0:
            if dbg:
                print("Command executed successfully:")
                print(result.stdout)
            return result.stdout
        else:
            print("Error executing the command:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to perform file copying and checks
def copy_files(dir_dict, class_list, args):
    # Get the path of the currently running Python script
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_script_path)

    for _type in dir_dict:
        for _dir in dir_dict[_type]:
            for _cls in class_list:
                file_name_src = f'{_type}/{args.mode}/back_{_cls}.png'
                file_name_dst = f'../cardtypes/{_dir}/back_{_cls}.png'

                if os.path.isfile(file_name_src):
                    cmd = f'identify {file_name_src}'
                    run_system_command(cmd)

                    try:
                        shutil.copy(file_name_src, file_name_dst)
                        print(f"File '{file_name_src}' copied to '{file_name_dst}'")
                    except shutil.Error as e:
                        print(f"Error copying '{file_name_src}' to '{file_name_dst}': {e}")
                else:
                    print(f"ERROR: The file '{file_name_src}' either does not exist or is not a regular file.")


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description='Select style of hero frame to use',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='Happy card creation'
    )

    # Define the command-line arguments
    parser.add_argument("mode",
                        choices=['orig', 'edge'],
                        help="Hero frame styles: orig (original), edge (better for bleed)"
    )

    parser.add_argument('-d', '--dbg', '--debug',
                        action='store_true',
                        help='Debug mode',
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    dir_dict      = {
        'common'   : ['hero_common', 'hero_common_transformed', 'hero_common_token', 'frbreak_hero_common', 'special_sidekick'],
        'uncommon' : ['hero_uncommon', 'hero_uncommon_transformed', 'frbreak_hero_uncommon'],
    }

    class_list   = ['none', 'covert', 'instinct', 'range', 'strength', 'tech']

    copy_files(dir_dict, class_list, args)
    print(f'Frame style: {args.mode} setup.')


if __name__ == "__main__":
    main()
