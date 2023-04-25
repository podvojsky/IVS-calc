package:
	python3 setup.py --command-packages=stdeb.command bdist_deb

test_package: package
	echo "ivs" | sudo -S apt remove -y python3-ivscalc && sudo dpkg -i ./deb_dist/python3-ivscalc_1.0.0-1_all.deb && ivscalc

install: package
	echo "ivs" | sudo -S apt install -y python3-tk && sudo dpkg -i ./deb_dist/python3-ivscalc_1.0.0-1_all.deb
