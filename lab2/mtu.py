import os
import sys
import re

def is_valid(hostname):
    if hostname[-1] == ".":
        hostname = hostname[:-1]
    if len(hostname) > 253 or len(hostname) < 1:
        return False
    ldh_re = re.compile('^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$', re.IGNORECASE)
    return all(ldh_re.match(x) for x in hostname.split('.'))
        
        
        
l = 0
r = 10000
hostname = None
if len(sys.argv) > 1:
    hostname = sys.argv[1]

if (hostname is None or hostname == ''):
    hostname = os.environ.get('PINGHOSTNAME')

if (hostname is None or hostname == ''):
    print('ERROR: Invalid usage: PINGHOSTNAME ENV variable or first ARG must be set')
    exit(1)
if not is_valid(hostname):
    print('ERROR: Invalid hostname')
    exit(1)

response = os.system('ping -c 5 -s ' + str(0) + ' ' + hostname + ' >/dev/null 2>&1')
if response != 0:
    response = os.system('ping -c 5 -s ' + str(0) + ' ' + '8.8.8.8' + ' >/dev/null 2>&1')
    if response != 0:
        response = os.system('ping -c 5 -s ' + str(0) + ' ' + 'ya.ru' + ' >/dev/null 2>&1')
        if response != 0:
            print('ERROR: ICMP or everything is probably blocked')
        else:
            print('ERROR: Not reachable or non-existent')
    else:
        print('ERROR: Not reachable or non-existent')
    exit(1)
while l < r - 1:
    sz = (l + r) // 2
    print('Current testing MTU: ', sz + 28)
    response = os.system('ping -c 3 -s ' + str(sz) + ' ' + hostname + ' >/dev/null 2>&1')
    if response == 0:
        l = sz
    else:
        r = sz
if (l == 9999):
    print('SUCCESS: Min MTU undefined: unrouted self-pinging')
else:
    print('SUCCESS: Min MTU for hostname', hostname, ': ', l + 28)
