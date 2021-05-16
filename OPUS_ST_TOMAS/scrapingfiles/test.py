import os

cwd = os.getcwd()  # Get the current working directory (cwd)
print(f"cwd: {cwd}")
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))