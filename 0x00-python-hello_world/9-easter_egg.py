#!/usr/bin/python3
f = open('zen.txt')
string = f.read().rstrip('\n')
print(string)
f.close()
