import time
s = ""
arr = [chr(i) for i in range(ord('a'), ord('z') + 1)]
x = "hello world"

for i in range(len(x)):
    for j in range(len(arr)):
        print(s + arr[j])
        time.sleep(0.02)
        if arr[j] == x[i]:
            s += x[i]
            break