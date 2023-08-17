#!/usr/bin/python3
"""A module that reads stdin line by line and computes metrics"""
import sys
import signal


def print_stats(file_size, status_codes):
    """Prints the statistics"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


def signal_handler(sig, frame):
    """Handles SIGINT"""
    print_stats(file_size, status_codes)
    

if __name__ == "__main__":
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    i = 0
    try:
        for line in sys.stdin:
            parsed_line = line.split()
            if len(parsed_line) > 2:
                file_size += int(parsed_line[-1])
                if parsed_line[-2] in status_codes:
                    status_codes[parsed_line[-2]] += 1
            if i % 10 == 0:
                print_stats(file_size, status_codes)
            i += 1
    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, signal_handler)
        raise
    print_stats(file_size, status_codes)