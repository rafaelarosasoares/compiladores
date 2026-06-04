import sys
from antlr4 import FileStream, CommonTokenStream

sys.path.append("generated/grammar")
sys.path.append("src")

from HomiLexer import HomiLexer
from HomiParser import HomiParser

from ast_builder import AstBuilder
from semantic import SemanticAnalyzer
from yaml_generator import YamlGenerator


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

    syntax_errors = parser.getNumberOfSyntaxErrors()

    if syntax_errors > 0:
        print(f"Análise sintática encontrou {syntax_errors} erro(s).")
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
        semantic_analyzer.symbol_table
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