import os

HERE = os.getcwd()

def create_dir(dir_name, dir_path=HERE):
	try:
		parent_path = os.path.join(dir_path, dir_name)
		os.mkdir(parent_path)
		return parent_path
	except OSError:
		print("Failed directory creation")

def create_file(file_parent_dir, file_name, file_content):
	file_path = os.path.join(file_parent_dir, file_name)
	with open(file_path, "w+") as f:
		for content_line in file_content:
			f.write(content_line)
