import re
for _ in range(int(input().strip())):
    print('YES' if re.search(
        r'.*?'.join(list("hackerrank")), input().strip()) else 'NO')
