# SpaceBattle

This is a game made by following a tutorial by [Tech With Tim](https://www.youtube.com/watch?v=jO6qQDNa2UY&t=1194s). Do check him out on youtube.

The main code for the game is in SpaceBattle.py. setup.py is used to create the executable and installer files. Although the build file is not included in the repository the installer will install the files directly on your software.

## Creating build files

I would recommend using PyIsntaller. However I have used cx_Freeze. Inorder to make use of the setup file cx_Freeze needs to be installed.

### To install cx_Freeze:

> `pip install cx_Freeze`

### building executable and installer:

Once you have cx_Freeze installed use the command(s) bellow:

> `python setup.py build`

The command above will make a folder with an EXE in it.

> `python setup.py bdist_msi`

This will build an installer so that you can install it on a computer without python.
