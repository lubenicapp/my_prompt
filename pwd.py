#! /usr/bin/env python3
import subprocess
from socket import gethostname
import os
import sys
import time

# export PS1="$(python pwd.py)"

# ┌─ ─ ─┐
# └─ ─ ─┘
# ├─ ─ ─┤


STYLES = {
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "BLINK": "\033[5m",
    "INVERSE": "\033[7m",
    "STRIKETHROUGH": "\033[9m",
    "BOLD_OFF": "\033[22m",
    "UNDERLINE_OFF": "\033[24m",
    "BLINK_OFF": "\033[25m",
    "INVERSE_OFF": "\033[27m",
    "STRIKETHROUGH_OFF": "\033[29m",
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "RESET": "\033[0m",
    "PURPLE": "\u001b[38;5;98m",
    "DOGE": "\u001b[38;5;226m"
}


def prompt():
    p = [
        '┌─ ',
        s('GREEN', f"🕑{time.strftime('%H:%M')}"),
        ' ',
        s('DOGE', dogecoin()),
        s('PURPLE', get_venv()),
        s('WHITE', current_git_branch()),
        s('CYAN', s('BOLD', user_hostname())),
        ':',
        '\n└─ ',
        s('BLUE', working_directory()),
        s('MAGENTA', s('BOLD', permission())),
        ' '
    ]
    print(''.join(p))


def s(style, text):
    return f"{STYLES[style]}{text}{STYLES['RESET']}"


def permission():
    if os.getuid() == 0:
        return '>'
    return '>💲'


def current_git_branch():
    result = subprocess.run(["git", "branch", "--show-current"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    branch = result.stdout.decode().strip()
    if len(branch) > 0:
        return f"({branch}) "
    return ''


def user_hostname():
    username = os.environ['USER']
    hostname = gethostname()
    return f"{username}@{hostname}"


def working_directory():
    homedir = os.path.expanduser('~')
    wd = os.getcwd().replace(homedir, '~', 1)
    sp = wd.split('/')
    wd = '/'.join([s[0] for s in sp[0:-1] if len(s) > 0]) + f'/{sp[-1]}'
    return f"{wd}"


def get_venv():
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path is not None:
        return f"({venv_path.split('/')[-1]}) "
    return ''


def dogecoin():
    try:
        import requests
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd", timeout=5)
        if response.status_code == 200:
            value = response.json().get('dogecoin', '').get('usd', '')
            return '🐕' + str(round(float(value), 3)) + ' '
        return ''
    except Exception:
        return ''


prompt()
