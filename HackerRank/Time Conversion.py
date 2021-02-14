def timeConversion(s):
    if "PM" in s:  s = s.strip("PM")
    elif "AM" in s: s = s.strip("AM")

    s = list(map(int, s.split(":")))

    s[0] += 12
    if s[0] == 24: s[0] = 0
    elif s[0] > 24: s[0] -= 24

    s = "{0:02d}:{1:02d}:{2:02d}".format(s[0], s[1], s[2])
    return s  

# map, list, format 다시 공부하고 코드 수정 
def timeConversion(s):
    h, m, sec = map(int, s[:-2].split(":"))

    h = h%12 + (s[-2:]=='PM')*12
    s = "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)
    
    return s