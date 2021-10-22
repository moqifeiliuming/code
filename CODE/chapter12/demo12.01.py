import sys
sys.path.append('./test')

import my
my.greet('Bill')
#print(sys.modules)
print(sys.modules['my'])
print(type(sys.modules['my']))
print(sys.platform)

print(sys.argv[0])

if len(sys.argv) == 2:
    print(sys.argv[1])
    my.greet(sys.argv[1])

s = sys.stdin.read(6)
print(s)
sys.stdout.writelines('hello world')
print()
sys.stderr.writelines('error')

sys.exit(123)



