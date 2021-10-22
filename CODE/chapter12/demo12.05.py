import os
import subprocess
print(os.sep)
print(os.pathsep)
print(os.name)

print(os.environ)
print(os.environ['PATH'])
print(os.getenv('PATH'))
output = subprocess.getstatusoutput('exe')
print(output)
os.putenv('PATH', os.getenv('PATH') + os.pathsep+ '/temp/exe')


output = subprocess.getstatusoutput('exe')
print(output)
print(os.getenv('PATH'))

os.system('ls -al')

