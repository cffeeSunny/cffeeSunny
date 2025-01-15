def collatzSteps(n: int) -> int:
    acc=0
    while n!=1:
            if n%2==0:
                acc = acc+1
                n = n// 2
            else:
                acc = acc + 1
                n = n*3+1
    return acc
    pass
