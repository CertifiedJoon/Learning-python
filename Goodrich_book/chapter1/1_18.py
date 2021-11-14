def increasing_step():
    stepi = 2
    yieldi = 0
    while True :
        yield yieldi
        yieldi += stepi
        stepi += 2

        
gen = increasing_step()
print([next(gen) for _ in range(10)])