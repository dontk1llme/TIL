# 1440. 데일리실습 5-1. 요청과 썩은 과일 찾기 예제 Lv1

import random
def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:
		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
			card_list.append((shape, number))
	return card_list

trump_card_list = making_card_list()
alphabet={'A':14, 'K':13,'Q':12,'J':11, 10:10,9:9,8:8,7:7,6:6,5:5,4:4,3:3,2:2,1:1}
shape={'spade':4, 'diamond':3, 'heart':2, 'clover':1}
p1count=0
p2count=0

while True:
	player1 = random.choice(trump_card_list)
	trump_card_list.remove(player1)
	player2 = random.choice(trump_card_list)

	if alphabet[player1[1]] > alphabet[player2[1]]:
		print(f'{player1} {player2} player1 win!')
		p1count+=1
	elif alphabet[player1[1]] < alphabet[player2[1]]:
		print(f'{player1} {player2} player2 win!')
		p2count+=1
	elif alphabet[player1[1]] == alphabet[player2[1]]:
		if shape[player1[0]] > shape[player2[0]]:
			print(f'{player1} {player2} player1 win!')
			p1count+=1
		else:
			print(f'{player1} {player2} player2 win!')
			p2count+=1
	if p1count==6 or p2count==6: break
	

if p1count>p2count: print(f'{p1count}:{p2count} player1 win')
else: print(f'{p1count}:{p2count} player2 win')


	
