if __name__ == '__main__':
    n = int(input())
    nums_in = input()
    nums_split = nums_in.split()
    nums = map(int, nums_split)

    print(sorted(list(set(nums)))[-2])