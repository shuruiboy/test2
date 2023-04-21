def parse_while_loop(tokens):
    # Make sure the token list starts with "while"
    if tokens[0] != "while":
        return False
    
    # Find the index of the closing parenthesis
    closing_paren_index = find_closing_paren(tokens, 1)
    if closing_paren_index == -1:
        return False
    
    # Parse the boolean expression inside the parentheses
    bool_expr_tokens = tokens[2:closing_paren_index]
    if not parse_bool_expr(bool_expr_tokens):
        return False
    
    # Parse the block inside the while loop
    block_tokens = tokens[closing_paren_index+1:]
    if not parse_block(block_tokens):
        return False
    
    return True
