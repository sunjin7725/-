import re
s = '}]()[{'






answer = 0
pattern = re.compile('(\[\])|(\(\))|(\{\})')
for i in range(len(s)):
    print(s)
    pattern = re.compile('(\[\])|(\(\))|(\{\})')
    if len(re.sub(pattern, '', s)) == 0:
        answer += 1
    s = s[1:] + s[:1]
print(answer)