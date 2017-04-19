#!/user/bin/env python3

import os
import sys
import time
from datetime import datetime, timedelta
from . import timeManipulation


def __check_args__():
    directory = None
    time_delay = None
    if len(sys.argv) > 1:
        count = 1
        try:
            while sys.argv[count]:
                # Checking to see if the first character is a -, indicating argument type will follow
                if sys.argv[count][0] == '-':
                    # If the - was the first character, getting the second character for instruction type
                    if sys.argv[count][1] == 'd':
                        # -d sets the directory to monitor
                        directory = sys.argv[count + 1]
                        if not os.path.isdir(directory):
                            raise NotADirectoryError
                    elif sys.argv[count][1] == 't':
                        # -t sets the time between last edit and deletion
                        time_delay = timeManipulation.string_to_seconds(sys.argv[count + 1])
                    elif 'help' in sys.argv[count]:
                        print("""Monitors a directory and deletes files older than a specified age from last edit.
    -d\t\t Directory to monitor for old files
    -t\t\t Time between last edit to the file and file deletion format: '32d' or '4h' or '5m'
    \t\t    Note: currently only supports Days (d) Hours (h) or Minutes (m)
    --help\t Displays this help text""")
                count += 2
        except IndexError:
            print("Arguemnt error. Try checking any arguments passed and run again.")
        except NotADirectoryError:
            print("{dir} is not a valid directory. Please try again.".format(dir=directory))
        except NotImplementedError:
            print("Decimals and time other than second / minute / hour / day are not currently supported")
        except TypeError:
            print("Something went wrong. String was not passed to evaluation method")
        finally:
            print("Type --help for more information")
            exit()
    return {'dir': directory, 'time': time_delay}


def main():
    arg_info = __check_args__()
    # Set defaults if no arguments were provided
    if not arg_info['dir']:
        arg_info['dir'] = './'
    if not arg_info['time']:
        arg_info['time'] = 3600
    while True:
        # Infinite loop, checking for old files
        for file in os.listdir(arg_info['dir']):
            try:
                # Check what time the file was last modified
                mod_time = datetime.fromtimestamp(os.path.getmtime(file))
                # if the current time is after the time the file was modified with the buffer specified
                if datetime.now() > (mod_time + timedelta(seconds=arg_info['time'])):
                    # Delete the file
                    os.remove(file)
            except PermissionError:
                print("need higher permissions")
            except OSError:
                print("something went wrong in getting modified time")
        time.sleep(1)


if __name__ == '__main__':
    main()
