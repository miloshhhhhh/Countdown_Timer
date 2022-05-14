# timer 
import time
import sys

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('\nTime up!')


if __name__ == '__main__':
    countdown(int(sys.argv[1]))
