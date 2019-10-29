from os import environ
from sys import platform

from cx_Freeze import setup, Executable

environ['TCL_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'
environ['TK_LIBRARY'] = r'.\venv_win\Lib\tcl8.6'

base = None
if platform == 'win32':
    base = 'Win32GUI'

build_options = {
    'packages': ('pygame', )
}

executable = [Executable('./Main.py', base=base, icon='./res/big slime.ico', targetName='Random-Mage-Battle.exe')]

setup(
    name='Random-Mage-Battle',
    version='1.0.0',
    description='SaNaE™',
    author='Yoon "MeKal" Seok Jun',
    options={'build_exe': build_options},
    executables=executable,
    requires=['pygame']
)