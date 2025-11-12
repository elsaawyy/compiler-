tokens = [
    # --- Egyptian Arabic Keywords ---
    ('DECLARE', r'متغير'),
    ('RETURN', r'ودي'),
    ('PRINT', r'(يسطا|قول|اطبع)'),
    ('INPUT', r'(هات|دخل)'),
    ('IF', r'لو'),
    ('ELSE', r'(الا|غير)'),
    ('AND', r'و'),
    ('OR', r'او'),

    # --- Comparison & Logical Operators ---
    ('EQ', r'=='),
    ('NE', r'!='),
    ('GT', r'>'),
    ('LT', r'<'),
    ('GTE', r'>='),
    ('LTE', r'<='),

    # --- Arithmetic ---
    ('ASSIGN', r'='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('MULT', r'\*'),
    ('DIV', r'/'),

    # --- Grouping ---
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),

    # --- Literals ---
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"([^"\\]|\\.)*"'),
    ('IDENTIFIER', r'[أ-يA-Za-z_][أ-يA-Za-z_0-9]*'),

    # --- Comments & Whitespace ---
    ('COMMENT', r'#.*'),
    ('SPACE', r'[ \t]+'),
    ('NEWLINE', r'\n'),
]