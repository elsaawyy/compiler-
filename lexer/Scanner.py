import re
from lexer.token_definitions import tokens

# ✅ Precompile the combined regex for better performance
token_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens))

def tokenize(code):
    """
    Tokenize Egyptian Arabic source code.
    Yields tuples: (token_type, token_value, line_number, column_number)
    """
    line_num = 1
    line_start = 0
    pos = 0
    length = len(code)

    while pos < length:
        match = token_regex.match(code, pos)
        if not match:
            # Unrecognized token → throw syntax error
            raise SyntaxError(f"Unexpected character {code[pos]!r} at line {line_num}, col {pos - line_start + 1}")

        kind = match.lastgroup
        value = match.group()
        column = match.start() - line_start + 1
        pos = match.end()

        # Skip spaces, newlines, and comments
        if kind == 'NEWLINE':
            line_num += 1
            line_start = pos
            continue
        if kind in ['SPACE', 'COMMENT']:
            continue

        yield kind, value, line_num, column

