import sys

n = int(sys.argv[1])
i = 0
twice = 0
mi = 1
f = open('out.txt', "w")
sys.stdout = f
while i <= n:
    print(str(i), ' ', str(twice), ' ', str(mi))
    i = i + 1
    twice = 2 * i
    mi = 2 ** i
sys.stdout = sys.stdout
print('done!')
