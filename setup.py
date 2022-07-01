import cx_Freeze as cf

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