s = 13420

hours = s // 3600 

s = s - (hours * 3600)

minutes = s // 60

seconds = s - (minutes * 60)

print '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

