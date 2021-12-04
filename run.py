import os
import sys
import random

def get_next_wallpaper(curr_path):

    lst_dir = os.listdir() 
    rand_index = random.randint(0, len(lst_dir) - 1)
    return lst_dir[rand_index]
    
def get_wall_dir():
  return "/Users/MYOUNG/Pictures/mmt"

def main():


  script = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file '"
  path = get_wall_dir()
  file = get_next_wallpaper(path)
  # print("FILE = ", file)
  script = script + path + "/" + file
  # print("SCRIPT = ", script)  
  os.system(script)


main()


