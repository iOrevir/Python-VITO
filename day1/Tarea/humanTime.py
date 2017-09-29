#!/usr/bin/ env python

#TODO get the string
#TODO divide string
#TODO check if it is hours, minutes or seconds
#TODO if hours then * by 3600
#TODO if minutes then * by 60
#TODO print total amount of seconds

if __name__ == '__main__':
    time = input('Dame el tiempo que quieres pasar a segundos (separado por comas): ')
    hours = 0
    minutes = 0
    seconds = 0
    time2 = time.split(',')
    print(time2)
    for s in time2:
        time3 = s.strip(' ')
        print(time3)
        if ('hours' in s or 'h' in s):
            hours = int(s[:2]) * 3600
        if ('minutes' in s or 'm' in s):
            minutes = int(s[:2]) * 60
        if ('seconds' in s or 's' in s):
            seconds = int(s[:2])
    print('Total amount of seconds: ' + str(hours + minutes + seconds))
