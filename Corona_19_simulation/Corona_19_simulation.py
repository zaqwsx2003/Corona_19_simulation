import turtle
import random

tur = []  # 사람
pos_x = [] # x좌표
pos_y = [] # y좌표
hwak_list = [] # 확진자
hwak_dt = [] # 확진 일자
day = 1 #날짜 "첫날 날짜"

N = 10 #처음 사람수
n = 1 #확진자 수
p = 0.2 #확진자와 접촉 후 감염 확률 {0.1 = 10%}
nMin = 1 #하루 접촉자 수
nMax = 5 #하루 최대 접촉자 수


i = 0
while True: #사람의 좌표 적용
    t1 = turtle.Turtle()
    if i == 0:
        screen = t1.getscreen()
        screen.setup(600,600) #화면 크기 600x600
    t1.shape("circle") #모양 : 동그라미
    t1.speed("fastest") #사람이 그려지는 속도 빠름
    t1.penup()


    tmp_x = random.randint(-250,250) #x 좌표에서 -250x250으로 랜덤 생성
    tmp_y = random.randint(-250,250) #y 좌표에서 -250x250으로 랜덤 생성
    t1.goto(tmp_x,tmp_y)

    #각 좌표들 사이의 거리가 1보다 작으면 다시 랜덤 생성 {각 좌표 당 사람 사이의 거리 생성}
    close_fg = False
    chk_cnt = len(pos_x) #사람의 수를 카운트
    for i in range(chk_cnt): #사람 수 만큼 반복
           ds = t1.distance(pos_x[i], pos_y[i]) #t1과 각 좌표를 비교 후 측정
           if ds <1: #만약 ds 즉 거리가 1보다 작은지 확인
               close_fg = True

    if close_fg:
        t1.hideturtle()
        print("근접 발생")
        continue

    tur.append(t1)
    pos_x.append(tmp_x)
    pos_y.append(tmp_y)
    i += 1
    print("t"+str(i),end=" ")

    if i >= N-1:
        break

    print(pos_x)
    print(pos_y)

# 1일차 감염자 붉은 색 표시
for i in range(n): # n = 최초 감염자 
    rnum = random.randrange(0, N)
    if hwak_list.count(rnum): #임의로 추출한 사람이 확진자 list에 있으면 사람 1명 증가 
        n += 1 
        continue
    tur[rnum].color("red") #만약 확진자 list에 확진자1명이 증가 안하면 반복 해서 빨강 
    print("1일차 감염자 : ", rnum)
    hwak_dt.append(1)#첫날

# 확진자 리스트를 날 별로 복사해서 반복문 실행 
day_hwak_list = hwak_list[:] #리스트 복사 { [:]는 리스트 전체 복사}
print("day_hwak_list:", day_hwak_list) #당일 확진자 리스트
print("hwak_list:", hwak_list) #전체 확진자 리스트 

while True:
    for i in day_hwak_list:
        print("확진자 : ", i )
        idx = i
        m = random.randrange(nMin, nMax+1)
        print("접촉자 : ", m, "명")

        # 확진자 기준 거리 계산, 리스트 생성
        ds_list = []
        ds_list.clear()
        for j in range(0, N):
            ds = tur[idx].distance(pos_x[j], pos_y[j])
            ds_list.append(ds)

        #확진자 본인의 거리는 0이지만, 최소 값 제외를 위해 1000 으로 입력 
        ds_list[idx] = 10000
        l = 0
        for j in range (0,N):
            tmp_idx = ds_list.index(min(ds_list)) #ds_list에서 최소값 을 찾고 index를 찾음
            if hwak_list.count(tmp_idx):
                ds_list[tmp_idx] = 10000
                l += 1
                continue
            else:
                print("접촉 : ", idx, "-", tmp_idx)
                ds_list[tmp_idx] = 10000
                
                #감염여부 판단, 기준확률
                rp = random.randrange(0,100) #0~100까지 난수 발생
                if rp < p*100: #0~70까지 나오면 확진자 
                    hwak_list.append(tmp_idx)
                    tur[tmp_idx].color("blue")
                    hwak_dt.append(day)
                    print("감염 : ", tmp_idx)
                l += 1
            # 접촉자 수가 차면 반복문 종료
            if l >= m:
                break
    
    print("day", day,"end")
    print("")
    day += 1

    day_hwak_list = hwak_list[:] #확진자 리스트에서 하루 확진자 복사
    print("day_hwak_list:", day_hwak_list)
    print("hwak_list:", hwak_list)

    if len(hwak_list) >= N-1: #모든 인원이 확진되면 시뮬레이션 종료
        break

#최종 확진자의 리스트 출력
print(hwak_list) 
print(hwak_dt)

#좌표 창 유지를 위해 작성
input()



 