import time

my_time = int(input("Enter a time: "))

for x in range(1,my_time, 1):
    seconds = x % 60
    minutes = int(x / 60) %60
    hours = int(x / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Times up")