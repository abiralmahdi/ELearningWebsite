from cx_Freeze import setup, Executable
import sys

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.


setup(name = "Imperia Educations" ,
   version = "0.1" ,
   description = "This is a online tutoring application" ,
   executables = [Executable("gui.py", base=base)])