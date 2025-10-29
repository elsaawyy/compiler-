import re
from lexer.token_definitions import tokens

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)

def tokenize(code):
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        
       
        if kind in ['SPACE', 'NEWLINE']:
            continue
        
        yield kind, value
