#!/user/bin/env python3

import os
import sys
import time
import platform
from datetime import datetime, timedelta
import timeManipulation


def __check_args__():
    directory = None
    time_delay = None
    if len(sys.argv) > 1:
        try:
            for i in range(0, len(sys.argv)):
                # Checking to see if the first character is a -, indicating argument type will follow
                if sys.argv[i][0] == '-':
                    # If the - was the first character, getting the second character for instruction type
                    if sys.argv[i][1] == 'd':
                        # -d sets the directory to monitor
                        directory = sys.argv[i + 1]
                        if not os.path.isdir(directory):
                            raise NotADirectoryError
                    elif sys.argv[i][1] == 't':
                        # -t sets the time between last edit and deletion
                        time_delay = timeManipulation.string_to_seconds(sys.argv[i + 1])
                    elif 'help' in sys.argv[i]:
                        print("""Monitors a directory and deletes files older than a specified age from last edit.\n
    -d\t\t Directory to monitor for old files
    -t\t\t Time between last edit to the file and file deletion format: '32d' or '4h' or '5m'
    \t\t    Note: currently only supports Days (d) Hours (h) or Minutes (m)
    --help\t Displays this help text\n""")
                        break
        except IndexError:
            print("Arguemnt error. Try checking any arguments passed and run again.")
            print("Type --help for more information")
        except NotADirectoryError:
            print("{dir} is not a valid directory. Please try again.".format(dir=directory))
            print("Type --help for more information")
        except NotImplementedError:
            print("Decimals and time other than second / minute / hour / day are not currently supported")
            print("Type --help for more information")
        except TypeError:
            print("Something went wrong. String was not passed to evaluation method")
            print("Type --help for more information")
    return {'dir': directory, 'time': time_delay}


def get_mod_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return datetime.fromtimestamp(os.path.getmtime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        return datetime.fromtimestamp(stat.st_mtime)


def main():
    arg_info = __check_args__()
    # Set defaults if no arguments were provided
    if not arg_info['dir']:
        arg_info['dir'] = './'
    if not arg_info['time']:
        arg_info['time'] = 3600
    death_note = []
    try:
        while True:
            # Infinite loop, checking for old files
            for file in os.listdir(arg_info['dir']):
                full_path = os.path.join(arg_info['dir'], file)
                mod_time = get_mod_date(full_path)
                try:
                    # if the current time is after the time the file was modified with the buffer specified
                    if datetime.now() > (mod_time + timedelta(seconds=arg_info['time'])) and 'timeDelete.py' not in file\
                            and '__init__.py' not in file and 'timeManipulation.py' not in file:
                        # Delete the file
                        os.remove(full_path)
                        death_note.append(file)
                        print("Deleted: {0}".format(full_path))
                except PermissionError:
                    print("need higher permissions")
                    exit()

            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping Monitor of {0}".format(arg_info['dir']))
        print("List of files deleted:")
        for file in death_note:
            print("  {0}".format(file))


if __name__ == '__main__':
    main()
