import os
from playsound import playsound
from time import sleep

def main():
    sleep(2)
    print('first sleep done')
    sleep(1)
    print('second sleep done')
    while True:
        sleep(60)
        os.chdir(os.getenv('USERPROFILE'))
        playsound('haha.mp3')
        sleep(540)


main()
