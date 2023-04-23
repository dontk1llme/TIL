import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL01_LEEYESEUL'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.



#5스테이지가 운으로 성공해서 max 75 찍은 코드

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]   
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]
    
    angle=0
    power=100
    dx = 0
    dy = 0
    gak = 0
    ban = 5.73/2
    
    #모든 경우의 수를 따지기로 했읍니다.
    # 1~4 스테이지까지는 하드코딩...
    # 5스테이지는 운빨이었음니다...
    if (balls[1][0] != -1):
        now = balls[1][0]
        dx = balls[1][0] - whiteBall_x - ban
        dy = balls[1][1] - whiteBall_y- ban
        
        gak = math.atan2(dy,dx)
        gak = gak*180 / math.pi
        angle=90-gak+0.5
        if now==120.0: #2스테이지
            angle=90-gak-3
        
    elif(balls[2][0] != -1):
        dx = balls[2][0] - whiteBall_x- ban
        dy = balls[2][1] - whiteBall_y- ban
        
        gak = math.atan2(dy,dx)
        gak = gak*180 / math.pi
        angle=90-gak
    elif(balls[3][0] != -1):
        now = balls[3][0]
        dx = balls[3][0] - whiteBall_x- ban
        dy = balls[3][1] - whiteBall_y- ban
        
        gak = math.atan2(dy,dx)
        gak = gak*180 / math.pi
        angle=90-gak
        angle+=0.5
        if now==10.000000: # +5: 4스3번 최적화... 다른 번호들까지 일반화는 불가함
            angle=90-gak+2
    elif(balls[4][0] != -1):
        dx = balls[4][0] - whiteBall_x- ban
        dy = balls[4][1] - whiteBall_y- ban
        
        gak = math.atan2(dy,dx)
        gak = gak*180 / math.pi
        angle=90-gak
    elif (balls[5][0] != -1):
        dx = balls[5][0] - whiteBall_x- ban
        dy = balls[5][1] - whiteBall_y- ban
        
        gak = math.atan2(dy,dx)
        gak = gak*180 / math.pi
        angle=90-gak
        angle+=0.5
    
   






    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')