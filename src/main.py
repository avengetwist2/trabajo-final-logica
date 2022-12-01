
# para que funcione la importacion src.....
import unittest
from sys import path
import subprocess
path.append("../../")


#import views.AdminViews




if __name__ == '__main__':
    #AdminViews
    subprocess.call("views\AdminViews.py", shell=True)