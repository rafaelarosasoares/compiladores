import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

sys.path.append("generated/grammar")
sys.path.append("src")

from HomiLexer import HomiLexer
from HomiParser import HomiParser

from ast_builder import AstBuilder
from semantic import SemanticAnalyzer
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

    parser = HomiParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_error_collector)
    tree = parser.programa()

    syntax_errors = parser.getNumberOfSyntaxErrors()

    if syntax_errors > 0 or syntax_error_collector.errors:
        print(
            f"Análise sintática encontrou "
            f"{max(syntax_errors, len(syntax_error_collector.errors))} erro(s)."
        )
        for error in syntax_error_collector.errors:
            print(f"- {error}")
        return

    print("Análise sintática concluída sem erros.")

    ast = AstBuilder().visit(tree)

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
