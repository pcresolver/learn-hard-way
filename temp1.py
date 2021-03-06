import sys

data = [
    [ 2, 4, 2, 2, 8, 2, 8, 2, 8, 2, 2, 4, 2 ], [ 2, 4, 2, 2, 8, 2, 8, 2, 8, 2, 2, 4, 2 ],
    [ 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2 ],
    [ 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2, 4, 2 ],
    [ 8, 2, 8, 2, 8, 2, 8, 2, 8 ], [ 8, 2, 8, 2, 8, 2, 8, 2, 8 ],
    [ 2, 4, 2, 2, 2, 4, 2, 2, 2, 8, 2, 11, 2 ], [ 2, 4, 2, 2, 2, 4, 2, 2, 2, 8, 2, 11, 2 ], [ 0 ],
    [ 2, 4, 2, 2, 8, 2, 2, 8, 2, 2, 8, 3, 8, 2, 2, 4, 2, 2, 8 ],
    [ 2, 4, 2, 2, 8, 2, 2, 8, 2, 2, 8, 3, 8, 2, 2, 4, 2, 2, 8 ],
    [ 2, 4, 2, 2, 2, 4, 2, 2, 2, 8, 2, 2, 2, 5, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 2 ],
    [ 2, 4, 2, 2, 2, 4, 2, 2, 2, 8, 2, 2, 2, 5, 2, 2, 2, 4, 2, 2, 2, 4, 2, 2, 8 ],
    [ 8, 2, 2, 4, 2, 2, 2, 8, 2, 2, 2, 5, 2, 2, 8, 2, 8, 2, 8 ],
    [ 8, 2, 2, 4, 2, 2, 2, 8, 2, 2, 2, 5, 2, 2, 8, 2, 8, 8, 2 ],
    [ 2, 4, 2, 2, 8, 2, 8, 2, 2, 2, 8, 3, 2, 4, 2, 5, 2, 5, 8 ],
    [ 2, 4, 2, 2, 8, 2, 8, 2, 2, 2, 8, 3, 2, 4, 2, 5, 2, 5, 8 ]
]

print()

for line in data:
    counter = 0
    for charcount in line:
        if counter % 2 == 0:
            char = '+'
        else:
            char = ' '
        line = char * charcount
        sys.stdout.write(line)
        counter += 1
    print()

print()