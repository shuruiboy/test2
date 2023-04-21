class Token:
    def __init__(self, token_type, lexeme):
        self.token_type = token_type
        self.lexeme = lexeme

    def __repr__(self):
        return f"{self.token_type}({self.lexeme})"


def parse(tokens):
    def match(token_type):
        nonlocal index
        if index >= len(tokens):
            return False
        if tokens[index].token_type == token_type:
            index += 1
            return True
        return False

    def DECLARE():
        if match('DATA_TYPE') and match('IDENTIFIER'):
            while match('COMMA') and match('IDENTIFIER'):
                pass
            return True
        return False

    index = 0
    return DECLARE()
