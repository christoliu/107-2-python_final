import subprocess
import datetime
nowtime = datetime.datetime.today()
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', '"' + str(nowtime) + '"'])
subprocess.call(["git", "push"])


