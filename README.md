# DBF_DBC_converter

```
python 'utf-8' codec can't decode byte 0xab in position 0: invalid start byte code example

Example 1: 'utf-8' codec can't decode byte 0x85 in position 715: invalid start byte

import pandas as pd

data = pd.read_csv(filename, encoding= 'unicode_escape')

Example 2: UnicodeDecodeError: 'utf-8' codec can't decode byte invalid start byte

# Use 'ISO-8859-1' instead of "utf-8" for decoding

text = open(fn, 'rb').read().decode('ISO-8859-1')

Tags:Python Example
```

# Python 3 - os.listdir() Method
```
#!/usr/bin/python3
import os, sys

# Open a file
path = "d:\\tmp\\"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print (file)
```

# Python String endswith() Method
```
The endswith() method returns True if the string ends with the specified value, otherwise False.

xt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)
```
# Python | os.path.splitext() method
```
Code: Use of os.path.splitext() method
# Python program to explain os.path.splitext() method 
    
# importing os module 
import os
  
# path
path = '/home/User/Desktop/file.txt'
  
# Split the path in 
# root and ext pair
root_ext = os.path.splitext(path)
  
# print root and ext
# of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1], "\n")
  
  
# path
path = '/home/User/Desktop/'
  
# Split the path in 
# root and ext pair
root_ext = os.path.splitext(path)
  
# print root and ext
# of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1])
Output:
root part of '/home/User/Desktop/file.txt': /home/User/Desktop/file
ext part of '/home/User/Desktop/file.txt': .txt
```

