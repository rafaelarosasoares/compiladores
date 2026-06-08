## Trabalho de Compiladores

- Realizado por Henrique Pozzebon e Rafaela da Rosa Soares

## Requisitos

- Python 3
- Java, para regenerar os arquivos do ANTLR
- `antlr-4.13.2-complete.jar`, ja incluido no projeto

## Instalacao

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execucao

```bash
python3 src/main.py examples/exemplo1.homi
```

Os YAMLs validos sao gerados em `outputs/`.

## Comandos uteis

```bash
make generate
make run-all
make test
```

## Estrutura

- `grammar/Homi.g4`: especificacao da linguagem e do lexer.
- `src/table_parser.py`: parser LL(1) por tabela preditiva.
- `src/semantic.py`: tabela de simbolos e verificacoes semanticas.
- `src/yaml_generator.py`: geracao de YAML para Home Assistant.
- `examples/`: exemplos validos e exemplos com erros.
