def parse_declare(tokens):
    def match(expected_type):
        nonlocal current_token
        if current_token and current_token.token_type == expected_type:
            current_token = next_token()
            return True
        return False
    
    def next_token():
        nonlocal current_token_index
        current_token_index += 1
        return tokens[current_token_index] if current_token_index < len(tokens) else None
    
    def ID_list():
        if match('IDENTIFIER'):
            while match('COMMA'):
                if not match('IDENTIFIER'):
                    return False
            return True
        return False
    
    current_token_index = 0
    current_token = tokens[current_token_index]
    
    if match('DATATYPE') and match('IDENTIFIER') and ID_list():
        return True
    
    return False

