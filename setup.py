from setuptools import setup

setup(
	name = "create_py_pkg",
	author = "Reinny Almonte",
	author_email = "reynsth@gmail.com",
	url = "https://github.com/jighdan/create_python_package",
	version = "0.1.0",
	entry_points = {
		"console_scripts": [
			"create_py_pkg = create_py_pkg.__main__:main"
		]
	}
)