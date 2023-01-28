import subprocess
from socket import gethostname
import os
import sys

# export PS1="$(python pwd.py)"

COLORS = {
    'RED': "\033[0;31m",
    'GREEN': "\033[0;32m",
    'YELLOW': "\033[0;33m",
    'BLUE': "\033[0;34m",
    'PURPLE': "\033[0;35m",
    'CYAN': "\033[0;36m",
    'WHITE': "\033[0;37m",
    'RESET': "\033[0m"
}


def prompt():
    p = f"{get_venv()}{current_git_branch()}{user_hostname()}:{working_directory()}$ "
    print(p)


def current_git_branch():
    result = subprocess.run(["git", "branch", "--show-current"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    branch = result.stdout.decode().strip()
    if len(branch) > 0:
        return f"{COLORS['WHITE']}({branch}){COLORS['RESET']} "
    return ''


def user_hostname():
    username = os.environ['USER']
    hostname = gethostname()
    return f"{COLORS['CYAN']}{username}@{hostname}{COLORS['RESET']}"


def working_directory():
    homedir = os.path.expanduser('~')
    wd = os.getcwd().replace(homedir, '~', 1)
    sp = wd.split('/')
    wd = '/'.join([s[0] for s in sp[0:-1] if len(s) > 0]) + f'/{sp[-1]}'
    if wd == '/':
        wd = '//'
    return f"{COLORS['BLUE']}{wd[1:]}{COLORS['RESET']}"


def get_venv():
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path is not None:
        return f"{COLORS['YELLOW']}({venv_path.split('/')[-1]}){COLORS['RESET']} "
    return ''


prompt()
