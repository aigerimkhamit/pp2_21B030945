import os

BASE_URL = 'C:/Users/Айжан/Desktop/Айгерим ноут/pp2_21B030945/lab6'

for root, dirs, files in os.walk(BASE_URL):
    print(root)
    print("Directories:", dirs)
    print("Files:", files)
    print("Directories and files:", dirs+files)
    exit()