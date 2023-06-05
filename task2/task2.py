import sys
import math

def main(x, y, r, dots):
    for dot_x, dot_y in dots:
        # length from dot to circle center (squared)
        dot_r_squared = (dot_x - x)**2 + (dot_y - y)**2
        r_squared = r**2
        if (dot_r_squared == r_squared):
            print(0)
        elif (dot_r_squared < r_squared):
            print(1)
        else:
            print(2)    

if __name__ == "__main__":
    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])
    with open(file1, 'r') as f:
        x, y = [float(value) for value in f.readline().split(" ")]
        r = float(f.readline().split(" ")[0])
    with open(file2, 'r') as f:
        dots = [[float(value) for value in line.split(" ")] for line in f.readlines()]
    out = main(x, y, r, dots)