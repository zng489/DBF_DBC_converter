import os
from simpledbf import Dbf5

dbf = Dbf5("ACBIBR10.dbf", codec='ISO-8859-1')
dbf.to_csv("qweqwe.csv")
#print("data/" + file + " converted to csv")
