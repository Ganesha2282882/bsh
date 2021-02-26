all: binary

binary:
	pyinstaller --onefile app.py
	cp dist/app .
	mv app bsh
	chmod +x bsh

install: binary
	cp bsh /usr/local/bin/bsh
	chmod 755 /usr/local/bin/bsh

uninstall:
	rm /usr/local/bin/bsh

clean:
	rm -rf app.spec bsh build dist __pycache__
