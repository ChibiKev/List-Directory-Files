import os
import sys
import json

# Take directory paths from where we want to record the files. py main.py "<directory>" "<directory>"
paths = sys.argv[1:]

# Where we are going to be storing the files
listOfFiles = []

# Loop through the paths and if it exist, save it in the list of files.
for path in paths:
  if os.path.exists(path):
    files = os.listdir(path)
    if files == 0:
      print("'" + path + "'" + " Has No Files")
    listOfFiles.append({
      "count": len(files),
      "directory": path,
      "files": files
    })
  else:
    print("'" + path + "'" + " Does Not Exist")

# Serializing json
json_object = json.dumps(listOfFiles, indent = 2)
 
# Writing to result.json
with open("result.json", "w") as outfile:
  outfile.write(json_object)