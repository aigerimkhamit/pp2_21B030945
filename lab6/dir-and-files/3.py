import os

target = '/Users/Айжан/Desktop/Айгерим ноут/pp2_21B030945/lab6'
# target1 = '/Users/Айжан/Desktop/Айгерим ноут/pp2_21B030945/lab7' dos not exist


if os.path.exists(target):
    print("exists")
    for root, dirs, files in os.walk(target):
        print("Dirs:", dirs) 
        print("Files:", files)
        exit()
else:
    print("does not exist")
