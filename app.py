import io
import eel
import subprocess
from subprocess import Popen

eel.init('web')

@eel.expose
def output(param):
	f = open("temp.py", "w")
	f.write(param)
	f.close()
	p = Popen(["python","temp.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
	output, errors = p.communicate()
	if errors:
		return errors
	else:
		return output

try:
    eel.start('index.html', size=(989,600))
except (SystemExit, MemoryError, KeyboardInterrupt):
    # We can do something here if needed
    # But if we don't catch these safely, the script will crash
    pass 

print ('This is printed when the window is closed!')