import os

def compile(file, icon):
    os.system("pip install pyinstaller")

    if icon == None:
        os.system(f"pyinstaller -F {file}")
    else:
        os.system(f"pyinstaller -F -i \"{icon}\" {file}")
