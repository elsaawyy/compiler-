from lexer.Scanner import tokenize
from parser.parser import Parser
from parser.tree_visualizer import TreeVisualizer
from parser.parser_utils import ParserError

if __name__ == "__main__":
    try:
        with open("examples/test.eg", encoding="utf-8") as f:
            code = f.read()

        print("Tokenizing...")
        tokens = list(tokenize(code))
        print(f"Found {len(tokens)} tokens")

        print("\nParsing...")
        parser = Parser(tokens)
        ast = parser.parse()

        print(" Parse successful!")
        visualizer = TreeVisualizer()
        print("\nParse Tree:")
        print(visualizer.visualize(ast))

    except ParserError as e:
        print(f" Parser Error: {e}")
    except SyntaxError as e:
        print(f" Syntax Error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
        import traceback
        traceback.print_exc()
