def parse_dot(dot_text):
    header_dot_text = dot_text[0 : dot_text.find("{")].split()
    body_dot_text = dot_text[dot_text.find("{") + 1 : dot_text.rfind("}")]

    validate_header_dot_text(header_dot_text)

    edge_rules = []
    rule_search_start_index = 0
    while body_dot_text.find("->", rule_search_start_index) > -1:
        edge_rule_index = body_dot_text.find("->", rule_search_start_index)
        edge_rule_origin_state_name = prev_word(body_dot_text, edge_rule_index - 1)
        edge_rule_destination_state_name = next_word(body_dot_text, edge_rule_index + len("->"))
        probability_rule_index = body_dot_text.find("=", body_dot_text.find("label", edge_rule_index))
        edge_rule_transition_probability = next_number(body_dot_text, probability_rule_index)

        edge_rules.append({
            'origin_state_name' : edge_rule_origin_state_name,
            'destination_state_name' : edge_rule_destination_state_name,
            'transition_probability' : float(edge_rule_transition_probability)
        })

        rule_search_start_index = edge_rule_index + 1

    return {
        'name' : header_dot_text[1],
        'edge_rules' : edge_rules
    }

def prev_word(document, curr_index):
    prev_word = ""

    WHITESPACE_SYMBOLS = [" ", "\n", "\t"]

    is_curr_char_whitespace_symbol = False
    for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
        if document[curr_index] == WHITESPACE_SYMBOL:
            is_curr_char_whitespace_symbol = True
    while is_curr_char_whitespace_symbol:
        curr_index -= 1
        is_curr_char_whitespace_symbol = False
        for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
            if document[curr_index] == WHITESPACE_SYMBOL:
                is_curr_char_whitespace_symbol = True

    is_curr_char_whitespace_symbol = False
    for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
        if document[curr_index] == WHITESPACE_SYMBOL:
            is_curr_char_whitespace_symbol = True
    while not is_curr_char_whitespace_symbol:
        prev_word = document[curr_index] + prev_word
        curr_index -= 1
        is_curr_char_whitespace_symbol = False
        for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
            if document[curr_index] == WHITESPACE_SYMBOL:
                is_curr_char_whitespace_symbol = True

    return prev_word

def next_word(document, curr_index):
    next_word = ""

    WHITESPACE_SYMBOLS = [" ", "\n", "\t"]

    is_curr_char_whitespace_symbol = False
    for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
        if document[curr_index] == WHITESPACE_SYMBOL:
            is_curr_char_whitespace_symbol = True
    while is_curr_char_whitespace_symbol:
        curr_index += 1
        is_curr_char_whitespace_symbol = False
        for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
            if document[curr_index] == WHITESPACE_SYMBOL:
                is_curr_char_whitespace_symbol = True

    is_curr_char_whitespace_symbol = False
    for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
        if document[curr_index] == WHITESPACE_SYMBOL:
            is_curr_char_whitespace_symbol = True
    while not is_curr_char_whitespace_symbol:
        next_word += document[curr_index]
        curr_index += 1
        is_curr_char_whitespace_symbol = False
        for WHITESPACE_SYMBOL in WHITESPACE_SYMBOLS:
            if document[curr_index] == WHITESPACE_SYMBOL:
                is_curr_char_whitespace_symbol = True

    return next_word

def next_number(document, curr_index):
    next_number = ""

    NUMBERS = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    is_curr_char_number = False
    for NUMBER in NUMBERS:
        if document[curr_index] == NUMBER:
            is_curr_char_number = True
    while not is_curr_char_number:
        curr_index += 1
        is_curr_char_number = False
        for NUMBER in NUMBERS:
            if document[curr_index] == NUMBER:
                is_curr_char_number = True

    is_curr_char_number = False
    for NUMBER in NUMBERS:
        if document[curr_index] == NUMBER:
            is_curr_char_number = True
    while is_curr_char_number:
        next_number += document[curr_index]
        curr_index += 1
        is_curr_char_number = False
        for NUMBER in NUMBERS:
            if document[curr_index] == NUMBER:
                is_curr_char_number = True

    return next_number

def validate_header_dot_text(header_dot_text):
    if len(header_dot_text) != 2:
        raise ValueError("Invalid DOT syntax")
    if header_dot_text[0] != "digraph":
        raise ValueError("Graph must be digraph")

def split_by(document, seperators):
    tokens = [document]
    for seperator in seperators:
        new_tokens = []
        for token in tokens:
            new_tokens.extend(str(token).split(seperator))
        tokens = [x for x in new_tokens if x != '']
    return tokens
