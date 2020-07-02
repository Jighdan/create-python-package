from . import args
from .files_generator import create_dir, create_file
from .files_content import install_content, main_content, gen_setup_content

def main():
	# parse argument
	package_title = args.name
	# initialize setup.py content
	setup_content = gen_setup_content(package_title)

	# dirs creation
	package_parent = create_dir(package_title)
	package_container = create_dir(package_title, package_parent)

	# files creation
	create_file(package_parent, "README.md", "")
	create_file(package_parent, "install.sh", install_content)
	create_file(package_parent, "setup.py", setup_content)
	
	create_file(package_container, "__init__.py", "")
	create_file(package_container, "__main__.py", main_content)

	print("Package created in {0}".format(package_parent))
