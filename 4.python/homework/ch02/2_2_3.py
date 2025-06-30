num = int(input())
result = str(num)

if num >= 1_000_000_000:
    result = str(num // 1_000_000_000) + 'G'
elif num >= 1_000_000:
    result = str(num // 1_000_000) + 'M'
elif num >= 1_000:
    result = str(num // 1_000) + 'k'
elif num >= 0:
    pass
     
print(result)