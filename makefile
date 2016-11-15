$(file).s: $(file).c
	cpp $(file).c $(file).cpp.c
	python compiler.py $(file).cpp.c
	rm $(file).cpp.c