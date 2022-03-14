import os
path = '/Users/Айжан/Desktop/Айгерим ноут/pp2_21B030945/lab6/dir-and-files'

print("existence:", os.path.exists(path))
print("readability:", os.access(path, os.R_OK))
print("writability:", os.access(path, os.W_OK))
print("executability:", os.access(path, os.X_OK))

# path1 = '/Users/Айжан/Desktop/Айгерим ноут/pp2_21B030945/lab5/dir-and-files'
# print("existence:", os.path.exists(path1))
# print("readability:", os.access(path1, os.R_OK))
# print("writability:", os.access(path1, os.W_OK))
# print("executability:", os.access(path1, os.X_OK))
