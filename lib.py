def ls(n):


    nums = [45, 55, 60, 37, 100, 105, 220]


    for i in nums:
        if i % n == 0:
            print(i)
        else:
            print("число с остатком")