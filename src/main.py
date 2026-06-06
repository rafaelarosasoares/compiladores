import sys
from pathlib import Path
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


def plural(count: int, singular: str, plural_form: str) -> str:
    return singular if count == 1 else plural_form


def main():
    if len(sys.argv) < 2:
        print("Passe um arquivo .homi para compilar.")
        print("Exemplo: python3 src/main.py examples/exemplo1.homi")
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
        error_count = len(syntax_error_collector.errors)
        print(
            f"Não consegui reconhecer todo o texto do arquivo "
            f"({error_count} {plural(error_count, 'erro léxico', 'erros léxicos')})."
        )
        for error in syntax_error_collector.errors:
            print(f"- {error}")
        return

    parser = TableParser(token_stream.tokens)
    ast = parser.parse()

    if parser.errors:
        error_count = len(parser.errors)
        print(
            f"Encontrei {error_count} "
            f"{plural(error_count, 'problema de sintaxe', 'problemas de sintaxe')}."
        )
        for error in parser.errors:
            print(f"- {error}")
        return

    print("Sintaxe ok.")

    semantic_analyzer = SemanticAnalyzer()
    semantic_errors = semantic_analyzer.analyze(ast)

    if semantic_errors:
        error_count = len(semantic_errors)
        print(
            f"\nEncontrei {error_count} "
            f"{plural(error_count, 'problema semântico', 'problemas semânticos')}."
        )
        for error in semantic_errors:
            print(f"- {error}")
        return

    print("Semântica ok.")
    print("Programa válido. Gerando YAML...")

    # Geração YAML
    generator = YamlGenerator(
        semantic_analyzer.symbol_table,
        semantic_analyzer.entity_id_table
    )

    for automation in ast.automations:

        yaml_text = generator.generate(
            automation
        )

        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)

        filename = output_dir / (
            automation.name.replace(" ", "_")
            + ".yaml"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(yaml_text)

        print(f"- Arquivo gerado: {filename}")


if __name__ == "__main__":
    main()
