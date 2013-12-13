update:
	rm -rf gears_stylus/node_modules
	cd gears_stylus && npm install stylus nib
	rm -rf gears_stylus/node_modules/.bin
