from sys import stdin, stdout

N   = stdin.readline()
N_A = set(stdin.readline().split())
M   = stdin.readline()
M_A = stdin.readline().split()

for i in M_A:
    stdout.write('1\n') if i in N_A else stdout.write('0\n')