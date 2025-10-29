tokens = [
    # keywords
    ('DECLARE', r'متغير'),
    ('RETURN', r'ودي'),
    ('PRINT', r'يسطا'),
    ('INPUT', r'هات'),
    ('IF', r'لو'),
    ('ELSE', r'الا'),
    ('AND', r'و'),
    ('OR', r'او'),

    # general tokens
    ('NUMBER', r'\d+'),
    ('IDENTIFIER', r'[أ-يA-Za-z_]+'),
    ('ASSIGN', r'='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULT', r'\*'),
    ('DIV', r'/'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('STRING', r'".*?"'),
    ('SPACE', r'[ \t]+'),
    ('NEWLINE', r'\n'),
]
