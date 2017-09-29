#!/usr/bin/env python

import sys

if __name__ == '__main__':
    seconds = int(input('¿Cuantos segundos quieres convertir? '))
    hours = 0
    minutes = 0
    while seconds/3600 >= 1:
        hours += 1
        seconds = seconds - 3600
    while seconds/60 >= 1:
        minutes += 1
        seconds = seconds - 60

    print('hours: ' + str(hours))
    print('minutes: ' + str(minutes))
    print('seconds: ' + str(seconds))

    print('HH:MM:SS')
    print('{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds))
