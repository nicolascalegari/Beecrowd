while True:
    try:
        A, B = map(int, input().split())

        if B > A:
            print("ok")
        else:
            print("no")
    except EOFError:
        break