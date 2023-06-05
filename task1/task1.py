import sys

def main(n, m):
    result = [1]
    if n == 1:
        return result
    i = m - 1
    while (array_i(i, n) != 1):
        result.append(array_i(i, n))
        i = i + m - 1
    return result

def array_i(i, n):
    if n == 0:
        return i
    return (i % n) + 1

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    out = main(n, m)
    print(''.join(str(i) for i in out))
