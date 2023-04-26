PYTHON = python3
CALC = calc_view.py
PACK_FOLDER = xpodvo00_xuhrec00_xistva03_xforma19

.PHONY: all clean

all:
	sudo apt install -y $(PYTHON) &&\
	sudo apt install -y $(PYTHON)-tk

pack: clean doc test
	rm -rf __pycache__ &&\
	mkdir ../$(PACK_FOLDER) &&\
	mkdir ../$(PACK_FOLDER)/doc &&\
	mkdir ../$(PACK_FOLDER)/install &&\
	mkdir ../$(PACK_FOLDER)/repo &&\
	cp -r ../doc/html/* ../$(PACK_FOLDER)/doc &&\
	cp ../packages/*.deb ../$(PACK_FOLDER)/install &&\
	cp -r ../mockup ../$(PACK_FOLDER)/repo &&\
	cp -r ../plan ../$(PACK_FOLDER)/repo &&\
	cp -r ../profiling ../$(PACK_FOLDER)/repo &&\
	cp -r ../src ../$(PACK_FOLDER)/repo &&\
	cp ../debugging.png ../$(PACK_FOLDER)/repo &&\
	cp ../dokumentace.pdf ../$(PACK_FOLDER)/repo &&\
	cp ../screenshot.png ../$(PACK_FOLDER)/repo &&\
	cp ../skutecnost.txt ../$(PACK_FOLDER)/repo &&\
	cp ../hodnoceni.txt ../$(PACK_FOLDER)/repo &&\
	cp ../README.md ../$(PACK_FOLDER)/repo &&\
	cp ../.gitignore ../$(PACK_FOLDER)/repo &&\
	cp ../.editorconfig ../$(PACK_FOLDER)/repo &&\
	cp -r ../.git ../$(PACK_FOLDER)/repo &&\
	cd .. && zip -r $(PACK_FOLDER).zip $(PACK_FOLDER) &&\
	rm -rf xpodvo00_xuhrec00_xistva03_xforma19
	
clean:
	rm -rf ../$(PACK_FOLDER).zip
	rm -rf ../$(PACK_FOLDER) &&\
	rm -rf __pycache__

test:
	$(PYTHON) -m unittest

doc:
	sudo apt install -y graphviz &&\
	sudo apt install -y doxygen &&\
	doxygen

run:
	$(PYTHON) calc_view.py
