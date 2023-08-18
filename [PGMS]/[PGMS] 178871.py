# 178871 달리기 경주

def solution(players, callings):
# 인덱스를 다 도니까 시간초과남. 숫자로 해야함
#     for i in callings:
#         for j in range(len(players)):
#             if i == players[j]:
#                 temp = players[j]
#                 players[j] = players[j-1]
#                 players[j-1]=temp
                
                
#     answer = players
#     return answer
   
    players_ranking = {player:int(idx) for idx, player in enumerate(players)}
    # {"mumu" : 0, "soe" : 1, "poe" : 2, "kai" : 3, "mine" : 4}
   
    for call in callings:
       
        current_rank = players_ranking[call]
        #현재등수
       
        players_ranking[call] -= 1
        players_ranking[players[current_rank-1]] += 1
        #{플레이어:등수} 등수 바꿔주기 // -1, +1
       
        players[current_rank-1], players[current_rank] = call, players[current_rank-1]
        #바꿔준 등수를 list인 players에 교차 대입
   
    return players
