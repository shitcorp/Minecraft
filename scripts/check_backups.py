from pathlib import Path 
import os, datetime

# CONFIG
__BACKUPS_FOLDER="mc-backups"
# maximum age of backup in days
__MAX_AGE=1
# - DO NOT EDIT GETS SET AUTOMATICALLY! -
__BACKUPS_PATH=f"./{__BACKUPS_FOLDER}" if "scripts" not in os.getcwd() else f"../{__BACKUPS_FOLDER}"

# Current Date
x =datetime.datetime.now()

def formatTime(year, month, day):
  return f"{year}{str(month).zfill(2)}{str(day).zfill(2)}"

def main():
  try:
    for child in Path(__BACKUPS_PATH).iterdir():
      if child.is_file() and ".tgz" in child.name:
        date_max_age = formatTime(x.year, x.month, x.day-__MAX_AGE)
        date = child.name.split("-")[1]
        if date < date_max_age:
          print("FILE TO REMOVE:  " + child.name)
          try:
            os.remove(os.path.join(__BACKUPS_PATH, child.name))
            print("FILE REMOVED:    " + child.name)
          except:
            print("ERROR TRYING TO REMOVE: " + child.name)
  except FileNotFoundError:
    print("Backups Path does not exist or you're in the wrong directory.")
    exit(255)
    
if __name__ == "__main__":
  main()