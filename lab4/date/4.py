from datetime import datetime
x1 = datetime(2018, 10, 12)
x2 = datetime(2018, 12, 24)
a = (x2 - x1).total_seconds()
print(a)
