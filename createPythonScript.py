# The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file.

def create_python_script(filename):
  import os
  comments = "# Start of a new Python program"
  with open(filename, "w") as f:
    f.write(comments)
    f.close()
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))