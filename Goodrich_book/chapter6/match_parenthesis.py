def matchParenthesis(expr):
    lefty = {'{' : '}', '(':')', '[',']'}
    s = []
    for c in expr:
        if c in lefty.keys():
            s.append(c)
        elif lefty[s[-1]] == c:
            s.pop()
        else:
            return false
    return not s