
# para que funcione la importacion src.....
from sys import path
import subprocess
path.append("../../")




if __name__ == '__main__':
    #AdminViews()
    subprocess.call("views\AdminViews.py", shell=True)