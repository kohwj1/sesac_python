safe_min, safe_max = map(int, input().rstrip().split())
temp_list = list(map(int,input().rstrip().split()))

for temperature in temp_list:
    if temperature == -999:
        break
    elif safe_min <= temperature <= safe_max:
        print('Nothing to report')
    else:
        print('Alert!')
        break