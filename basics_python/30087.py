# 30087
# 개최하는 세미나의 개수를 입력 받고 그 개수만큼 세미나 목록을 입력 받는다
# 해당 세미나가 어느 교실에 열리는 지 출력하기

semi = {"Algorithm": "204", "DataAnalysis": "207", "ArtificialIntelligence": "302",
        "CyberSecurity": "B101", "Network": "303", "Startup": "501",
        "TestStrategy": "105"}


n = int(input())

for i in range(n):
    name = input()
    print(semi[name])