PYTHON ?= python3
ANTLR_JAR ?= antlr-4.13.2-complete.jar
GRAMMAR ?= grammar/Homi.g4

.PHONY: generate run-example run-all test clean

generate:
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor $(GRAMMAR) -o generated

run-example:
	$(PYTHON) src/main.py examples/exemplo1.homi

run-all:
	@for file in examples/exemplo*.homi; do \
		echo "==> $$file"; \
		$(PYTHON) src/main.py "$$file"; \
	done

test:
	$(PYTHON) src/main.py examples/erro_sintatico.homi
	$(PYTHON) src/main.py examples/erro_sintatico_multiplos.homi
	$(PYTHON) src/main.py examples/erro_semantico.homi
	$(PYTHON) src/main.py examples/erro_semantico_condicao.homi

clean:
	rm -f outputs/*.yaml
