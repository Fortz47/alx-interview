#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import re
import signal
import os


def log_stat(stats, file_size):
    """logs stats to stdout"""
    print('File size: {}'.format(file_size))
    for k, v in stats.items():
        print("{}: {}".format(k, v))


codes = ['200', '301', '400', '401', '403', '404', '405', '500']
stats = {}

file_size = 0
ip = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
date = r'\[[\d-]+\s[\d:.]+\]'
req = r'"GET /projects/260 HTTP/1.1" ([0-9]{3}) ([0-9]+)$'
pattern = '{} - {} {}'.format(ip, date, req)
count = 0

while True:
    try:
        line = input().strip()
        result = re.match(pattern, line)
        if result:
            status_code = result.group(1)
            fileSize = result.group(2)
            if status_code in codes:
                if stats.get(status_code):
                    stats[status_code] += 1
                else:
                    stats[status_code] = 1
            file_size += int(fileSize)
            count += 1
            if count % 10 == 0:
                log_stat(stats, file_size)
    except EOFError:
        # EOF (end of file) reached
        break
    except KeyboardInterrupt:
        log_stat(stats, file_size)
        # os.kill(os.getpid(), signal.SIGINT)
        raise
