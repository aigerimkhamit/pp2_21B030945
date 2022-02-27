def func(numsheads, numslegs):
    # chicken - 2
    # rabbit - 4
    # if we think that, there is only chickens, then:
    w = numsheads * 2
    # then, we can say that 
    p = numslegs - w # лишние ноги, по голове на каждые две ноги
    #so, rabbits 
    x = p / 2
    #chickens
    y = numsheads - x
    print(int(y), int(x))

numsheads, numslegs = map(int, input().split())
func(numsheads, numslegs)
      