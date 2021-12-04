import os
import sys

def main():

  def f(curr):
    nonlocal count
    files_and_dirs = os.listdir(curr)
    dirs = []
    for element in files_and_dirs:
      path_filename = curr + element
      if element.endswith(".jpg") or element.endswith(".jpeg") or os.path.isdir(path_filename):
        if os.path.isdir(path_filename):
          dirs.append(element)
        else:
          path_filename = curr + element

          path_new_filename = curr + str(count) + '.jpg'
          count += 1
          
          while os.path.isfile(path_new_filename):
            path_new_filename = curr + str(count) + '.jpg'
            count += 1

          if os.path.isfile(path_filename):
            os.rename(path_filename, path_new_filename)

      for dr in dirs:
        f(curr + dr + '/')

  argc = len(sys.argv)
  if argc == 1:
    print("please provide directory")
  elif argc > 2:
    print("please provide only one command line argument")
  else:
    if os.path.isdir(sys.argv[1]) == False:
      print("directory not found")
    else:
      count = 0
      f(sys.argv[1] + '/')

main()
	
