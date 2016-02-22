# coding:utf-8
from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    # "packages": ["os"],
    # "includes": ["PIL", "draw9Patch"],
    "include_files": ["icon.ico"],
    "optimize": 2,
    "excludes": ["tkinter"]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
executable = [Executable("main.py",
                         base=base,
                         icon="icon.ico",
                         shortcutName="Draw9Path",
                         shortcutDir="DesktopFolder",
                         targetName='fastDraw9Path.exe')]
bdist_msi_options = {
    "add_to_path": True,
    "upgrade_code": "{886bd85e-c5ff-43df-a9d6-ce3f022382b1}"
}
setup(
    name='FastDraw9Patch',
    version='1.0.0',
    author='Jack_long',
    author_email='yuwenyishan@gmail.com',
    description='fast create .9 picture !',
    executables=executable,
    options={
        "bdist_msi": bdist_msi_options,
        "build_exe": build_exe_options}
)
