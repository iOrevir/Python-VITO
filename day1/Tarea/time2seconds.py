#!/usr/bin/env python

#TODO ask the professor what he meant (second problem)

if __name__ == '__main__':
    time = input('¿Cuanto tiempo quieres convertir a segundos?')
    hours = int(time[:2])
    minutes = int(time[3:5])
    seconds = int(time[6:])
    print('hours:' + str(hours))
    print('minutes: ' + str(minutes))
    print('seconds: ' + str(seconds))

    seconds = seconds + minutes*60 + hours*3600
    print('total seconds: ' + str(seconds))
