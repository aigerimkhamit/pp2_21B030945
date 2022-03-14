import os

path = '/Users/Айжан/Desktop/Айгерим ноут/pp2_21B030945/lab6/dir-and-files/delete'

if os.path.exists(path) and os.access(path, os.R_OK) and os.access(path, os.W_OK) and os.access(path, os.X_OK):
    os.rmdir(path)