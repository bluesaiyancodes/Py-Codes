if __name__ == '__main__':
    n = int(input())
    #for i in range(1,n+1):
    #    print(i, end='')

    b = ''

    for i in range(1,n+1):
        b = b + str(i)

    print(b)
    print(type(b))