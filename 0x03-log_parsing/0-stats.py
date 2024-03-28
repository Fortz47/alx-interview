#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import re
import signal


def handler(stats, file_size):
    """handles CTRL + C"""
    print('File size: {}'.format(file_size))
    for k, v in stats.items():
        print("{}: {}".format(k, v))

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}

file_size = 0
ip = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
date = r'[datetime.datetime\(.+\)]'
req = r'\"GET /projects/260 HTTP/1.1\" ([0-9]{3}) ([0-9]+)$'
pattern = '{} - {} {}'.format(ip, date, req)
count = 0
signal.signal(signal.CTRL_C_EVENT, handler)

while True:
    try:
        line = input().strip()
        result = re.match(pattern, line)
        if result:
            status_code = result.group(1)
            file_size = result.group(2)
            stats[status_code] += 1
            file_size += int(file_size)
            count += 1
            if count % 10 == 0:
                handler(stats, file_size)
    except EOFError:
        # EOF (end of file) reached
        break
