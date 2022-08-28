from sigfigs import Val

ops = {'+', '-', '*', '/', '^'}
paren = {'(', ')'}
precedence = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}

def tokenize(exp):
    exp = exp.replace(' ', '')
    while exp:
        i = 0
        while i < len(exp) and exp[i] not in ops and exp[i] not in paren:
            i += 1
        if i >= len(exp):
            ret = exp
            exp = None
            yield ret
            return

        if exp[i] in ops or exp[i] in paren:
            if i == 0:
                ret = exp[0]
                exp = exp[1:]
                yield ret
            else:
                ret = exp[:i]
                exp = exp[i:]
                yield ret

def run_op(operators, values):
    op = operators.pop()
    right, left = values.pop(), values.pop()
    if op == '+':
        values.append(left + right)
    if op == '-':
        values.append(left - right)
    if op == '*':
        values.append(left * right)
    if op == '/':
        values.append(left / right)
    if op == '^':
        values.append(left ^ right)

def peek(stack):
    return stack[-1] if stack else None

def greater_prec(opa, opb):
    return precedence[opa] > precedence[opb]

def seval(exp):
    tokens = tokenize(exp)
    values = []
    operators = []
    for tok in tokens:
        if tok.replace('.', '').isnumeric():
            values.append(Val(tok))
        elif tok == '(':
            operators.append('(')
        elif tok == ')':
            while (top := peek(operators)) is not None and top != '(':
                run_op(operators, values)
            operators.pop()
        else:
            while (top := peek(operators)) is not None and top not in '()' and greater_prec(top, tok):
                run_op(operators, values)
            operators.append(tok)
    while peek(operators) is not None:
        run_op(operators, values)

    return values[0]

