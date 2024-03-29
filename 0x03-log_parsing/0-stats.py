#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
# import re
# import sys


# def log_stat(stats, file_size):
#     """logs stats to stdout"""
#     print('File size: {}'.format(file_size))
#     for code in sorted(stats):
#         print("{}: {}".format(code, stats[code]))


# codes = ['200', '301', '400', '401', '403', '404', '405', '500']
# stats = {}

# file_size = 0
# ip = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
# date = r'\[[\d-]+\s[\d:.]+\]'
# req = r'"GET /projects/260 HTTP/1.1" ([0-9]{3}) ([0-9]+)$'
# pattern = '{} - {} {}'.format(ip, date, req)
# count = 0

# try:
#     for line in sys.stdin:
#         result = re.match(pattern, line)
#         if result:
#             status_code = result.group(1)
#             fileSize = result.group(2)
#             if status_code in codes:
#                 if stats.get(int(status_code)):
#                     stats[int(status_code)] += 1
#                 else:
#                     stats[int(status_code)] = 1
#             file_size += int(fileSize)
#         count += 1
#         if count % 10 == 0:
#             log_stat(stats, file_size)
#     log_stat(stats, file_size)
# except KeyboardInterrupt:
#     log_stat(stats, file_size)
#     raise
def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
