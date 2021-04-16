import time

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

initial = time.time()
k = 0
while(k<45):
    print("yo yo honey singh")
    time.sleep(1)  # it atop programme for 2 sec
    k += 1
print(f"while loop takes{time.time() - initial} seconds to run")
    
initial2 = time.time()
for i in range(45):
    print("sub boy baadshah")
print(f"while loop takes {time.time() - initial2} seconds to run")


    