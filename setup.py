import cx_Freeze as cf
import os


# Assets to be included

RSS = os.path.join('Assets', 'spaceship_red.png')
YSS = os.path.join('Assets', 'spaceship_yellow.png')
HS = os.path.join('Assets', 'Gun+Silencer.mp3')
FS = os.path.join('Assets', 'Grenade+1.mp3')


executables = [cf.Executable("main.py")]

cf.setup(

    name = "Space Battle",
    version ="0.1",
    description = "Testing pygame",
    options = {"build_exe": {
                                "packages" : ["pygame", "os"],
                                "include_files": ["Assets/"]
                                
                                }},
    executables = executables
)