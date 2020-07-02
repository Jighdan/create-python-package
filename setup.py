from setuptools import setup

setup(
	name = "create_python_pkg",
	author = "Reinny Almonte",
	author_email = "reynsth@gmail.com",
	url = "https://github.com/jighdan/create_python_package",
        description = "A simple python package template generator",
	version = "0.1.0",
	entry_points = {
		"console_scripts": [
			"create_python_pkg = create_python_pkg.__main__:main"
		]
	},
        python_requires=">=3.6"
)
