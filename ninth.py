def parse_bool_expr(tokens):
    def parse_bterm():
        res = parse_band()
        while tokens and tokens[0].value in ('==', '!='):
            op_token = tokens.pop(0)
            rhs = parse_band()
            res = (op_token.value, res, rhs)
        return res

    def parse_band():
        res = parse_bor()
        while tokens and tokens[0].value == '&&':
            op_token = tokens.pop(0)
            rhs = parse_bor()
            res = (op_token.value, res, rhs)
        return res

    def parse_bor():
        res = parse_expr()
        while tokens and tokens[0].value == '||':
            op_token = tokens.pop(0)
            rhs = parse_expr()
            res = (op_token.value, res, rhs)
        return res

    def parse_expr():
        res = parse_term()
        while tokens and tokens[0].value in ('+', '-', '*', '/', '%'):
            op_token = tokens.pop(0)
            rhs = parse_term()
            res = (op_token.value, res, rhs)
        return res

    def parse_term():
        res = parse_fact()
        while tokens and tokens[0].value in ('*', '/', '%'):
            op_token = tokens.pop(0)
            rhs = parse_fact()
            res = (op_token.value, res, rhs)
        return res

    def parse_fact():
        if not tokens:
            raise ValueError('Unexpected end of input')
        token = tokens.pop(0)
        if token.type == 'ID':
            return token.value
        elif token.type in ('INT_LIT', 'FLOAT_LIT'):
            return float(token.value)
        elif token.value == '(':
            res = parse_bool_expr(tokens)
            if not tokens or tokens.pop(0).value != ')':
                raise ValueError('Mismatched parentheses')
            return res
        else:
            raise ValueError('Invalid token: {}'.format(token.value))
