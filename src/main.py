import sys
from antlr4 import FileStream, CommonTokenStream

sys.path.append("generated/grammar")

from HomiLexer import HomiLexer
from HomiParser import HomiParser


def main():
    if len(sys.argv) < 2:
        print("Uso: python src/main.py arquivo.homi")
        return

    input_file = sys.argv[1]

    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = HomiLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = HomiParser(token_stream)

    tree = parser.programa()

    print("Parse concluído.")
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main()