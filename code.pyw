import os
from playsound import playsound
from time import sleep


def main():
    sleep(2)
    print('first sleep done')
    sleep(1)
    print('second sleep done')
    os.chdir(os.getenv('USERPROFILE'))
    if not os.path.exists('haha.mp3'):
        os._exit(1)
    while True:
        sleep(60)
        playsound('haha.mp3')
        sleep(540)


main()
