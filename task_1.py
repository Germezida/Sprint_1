base = '1h 45m,360s,25m,30m 120s,2h 60s'
time = base.split(',')
total = 0
for i in time:
    time_2 = i.split()
    for part in time_2:
        if 'h' in part:
            total += int(part.replace('h', '')) * 60
        elif 'm' in part:
            total += int(part.replace('m', ''))
        elif 's' in part:
            total += int(part.replace('s', ''))/60
print(total)