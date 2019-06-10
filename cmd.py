import subprocess
import datetime
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', '"It\'s ' + str(datetime.datetime.now()) + '"'])
subprocess.call(['git', 'push'])

