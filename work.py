# print("15.5".isdigit(), "15".isdigit())

try:
   t = "2000:2020"
   t = t.replace(":",",")
   r = t.split(",")
   print(r)
except ZeroDivisionError as r:
    print(r.args)
