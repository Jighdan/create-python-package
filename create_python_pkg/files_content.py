# install.sh content
install_content = [
	"pip install -e . || pip3 install -e .", 
	"\n"
	]

# _main__.py content 
main_content = [
	"# modules here", 
	"\n", 
	"\ndef main():", 
	"\n    pass", 
	"\n"
	]

# setup.py content
def gen_setup_content(package_title):
	setup_py = [
		"from setuptools import setup",
		"\n",
		"\nsetup(",
		"\n    name = {0}".format(package_title),
		"\n    version = 0.1.0",
		"\n    entry_points = {",
		"\n        'console_scripts': [",
		"\n            '{0}' = '{0}.__main__:main'".format(package_title),
		"\n        ]",
		"\n    }",
		"\n)",
		"\n"
	]

	return setup_py