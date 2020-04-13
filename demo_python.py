import time

my_list = ["Sean", "Dan", "Megan"]

print(my_list)

for name in my_list:
    print(name)

print("Done")


i = 0
while i < 10:
    print(i)
    i += 1
    time.sleep(1)


# Uncomment to run this (Caution: this is an infinite loop)
# while True:
#     print(time.time())
#     time.sleep(1)

print(my_list[0])
