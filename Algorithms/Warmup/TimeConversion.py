#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function

    time = s.rstrip('APM').split(':')
    
    if 'P' == s[8] and time[0] != '12':
        time[0] = int(time[0]) + 12
        time[0] = str(time[0])
    elif 'A' == s[8] and time[0] == '12':
        time[0] = '00'
        
    return ':'.join(time)
    
s = input().strip()
result = timeConversion(s)
print(result)
