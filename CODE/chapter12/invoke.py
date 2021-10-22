import subprocess
output = subprocess.getstatusoutput('python demo12.01.py Mike')
print(output)
print(output[0])