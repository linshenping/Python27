#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==1.1.6','console_scripts','easy_install'
__requires__ = 'setuptools==1.1.6'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('setuptools==1.1.6', 'console_scripts', 'easy_install')()
    )
