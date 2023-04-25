.PHONY: all clean

all:
	echo "ivs" | sudo -S apt install -y python3 &&\
	echo "ivs" | sudo -S apt install -y python3-tk

pack: clean
	mkdir tmp &&\
	cp ../doc/html/* ../tmp/doc &&\
	cp ../deb_dist/*.deb ../tmp/install &&\
	cp -r ../mockup ../tmp/repo &&\
	cp -r ../plan ../tmp/repo &&\
	cp -r ../profiling ../tmp/repo &&\
	cp -r ../src ../tmp/repo &&\
	cp ../debugging.png ../tmp/repo &&\
	cp ../dokumentace.pdf ../tmp/repo &&\
	cp ../screenshot.png ../tmp/repo &&\
	cp ../skutecnost.txt ../tmp/repo &&\
	cp ../hodnoceni.txt ../tmp/repo &&\
	cp ../README.md ../tmp/repo &&\
	cp ../.gitignore ../tmp/repo &&\
	cp ../.editorconfig ../tmp/repo &&\
	cp -r ../.git ../tmp/repo &&\
	cp ../src/hodnoceni.txt ../tmp
	
clean:
	rm -r __pycache__

test:
	python3 -m unittest

doc:
	echo "ivs" | sudo -S apt install -y graphviz &&\
	echo "ivs" | sudo -S apt install -y doxygen &&\
	doxygen

run:
	python3 calc_view.py
