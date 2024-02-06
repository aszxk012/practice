# 20232
# 1995년부터 2019년까지의 대회 우승자 명단이 주어진다.
# 입력한 년도에 우승한 우승자 출력

winner = ["ITMO", "SPbSU", "SPbSU", "ITMO", "ITMO",
          "SPbSU", "ITMO", "ITMO", "ITMO", "ITMO",
          "ITMO", "PetrSU, ITMO", "SPbSU", "SPbSU",
          "ITMO", "ITMO", "ITMO", "ITMO", "SPbSU",
          "ITMO", "ITMO", "ITMO", "ITMO", "SPbSU", "ITMO"]

year = int(input())
year -= 1995

print(winner[year])