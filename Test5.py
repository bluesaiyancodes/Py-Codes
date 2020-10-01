if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(arr)
    for k in range(0,n-1):
        if arr[k]>arr[k+1]:
            print(arr[k+1])
            exit()


