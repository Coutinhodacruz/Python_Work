s = "11111222223"
k = 3
result = ""

while len(s) > k:
    local_res = 0
    count = 0
    for i in range(len(s)):
        if count < k:
            local_res += int(s[i])
            count += 1
        else:
            result += str(local_res)
            count = 0
            local_res = 0
            local_res += int(s[i])
            count += 1
    result += str(local_res)
    s = result
    result = ""
print(s)
