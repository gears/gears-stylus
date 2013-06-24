update:
	rm -rf gears_stylus/node_modules
	cd gears_stylus && npm install stylus nib canvas
	rm -rf gears_stylus/node_modules/.bin
