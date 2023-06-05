import sys

def main(nums):
    avg = round(sum(nums) / len(nums))
    result = 0
    for n in nums:
        result += abs(n - avg)
    return result

if __name__ == "__main__":
    file1 = str(sys.argv[1])
    with open(file1, 'r') as f:
        nums = [int(n) for n in f.readlines()]
    print(main(nums))