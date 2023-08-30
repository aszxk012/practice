# 16170
# 세계 표준시 기준으로 오늘의 연도, 월, 일 한 줄에 하나씩 출력하기

from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
# timezone -> 시간대 정보 처리

print(today.year)
print("%02d" % (today.month))
print(today.day)