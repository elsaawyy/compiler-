from lexer.Scanner import tokenize

if __name__ == "__main__":
    with open("examples/test.eg", encoding="utf-8") as f:
        code = f.read()

    print("Tokens:")
    for token in tokenize(code):
        print(token)
