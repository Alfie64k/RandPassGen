import random

realKey = random.randint(1,10000)
with open("D:\\HomeComputing\\RandPassGen\\Password.txt",'w') as f:
    f.write("%d" % realKey)
f.close()

userKey = int(input("Please enter the password: "))
if userKey == realKey:
    print("You now have access to the files")
    with open("D:\\HomeComputing\\RandPassGen\\Data.txt",'w') as z:
        z.write("Test")
    z.close()