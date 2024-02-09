# import time, asyncio, datetime

# async def prin_str():
#     while True:
#         await asyncio.sleep(300-time.time()%300)
#         print("Hello")


# prin_str()

# t = ((2,3),(1,4),(5,6),(7,8),(10,0))
# import datetime 

# dateobj = datetime.datetime.now()

# print(dateobj.strftime("%d-%m-%y"))

d = {3:4, "aa":34, 45:"bb"}

for i in d.keys():
    if type(i) == str:
        print({i:d[i]})