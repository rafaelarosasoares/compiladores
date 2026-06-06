import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

sys.path.append("generated/grammar")
sys.path.append("src")

from HomiLexer import HomiLexer

from semantic import SemanticAnalyzer
from table_parser import TableParser
from yaml_generator import YamlGenerator


class SyntaxErrorCollector(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Linha {line}, coluna {column}: {msg}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python src/main.py arquivo.homi")
        return

    input_file = sys.argv[1]

    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = HomiLexer(input_stream)
    syntax_error_collector = SyntaxErrorCollector()
    lexer.removeErrorListeners()
    lexer.addErrorListener(syntax_error_collector)

    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    if syntax_error_collector.errors:
        print(
            f"Análise léxica encontrou "
            f"{len(syntax_error_collector.errors)} erro(s)."
        )
        for error in syntax_error_collector.errors:
            print(f"- {error}")
        return

    parser = TableParser(token_stream.tokens)
    ast = parser.parse()

    if parser.errors:
        print(f"Análise sintática encontrou {len(parser.errors)} erro(s).")
        for error in parser.errors:
            print(f"- {error}")
        return

    print("Análise sintática concluída sem erros.")

    semantic_analyzer = SemanticAnalyzer()
    semantic_errors = semantic_analyzer.analyze(ast)

    if semantic_errors:
        print("\nErros semânticos encontrados:")
        for error in semantic_errors:
            print(f"- {error}")
        return

    print("Análise semântica concluída sem erros.")
    print("Programa válido.")

    # Geração YAML
    generator = YamlGenerator(
        semantic_analyzer.symbol_table,
        semantic_analyzer.entity_id_table
    )

    for automation in ast.automations:

        yaml_text = generator.generate(
            automation
        )

        filename = (
            automation.name.replace(" ", "_")
            + ".yaml"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(yaml_text)

        print(f"YAML gerado: {filename}")


if __name__ == "__main__":
    main()
