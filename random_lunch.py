students =  [

    '기남석', '김경림', '김규리', '김동수', '김영식',

    '김영준', '김하늬', '류태규', '박시현', '박준하',

    '서영준', '신선호', '안예나', '양희진', '오지원',

    '유정훈', '이경진', '이여민', '이창준', '이한빈',

    '정석진', '정유정', '정효상', '조민주', '최종현'

    ]

# 결석하신 분ㅠㅠ & 점심 안 드실 분 빼기
absent = list(input('오늘 결석한 사람, 점심 안 먹을 사람: ').split()) 
for i in absent:
    if i in students:
        students.remove(i)

# 10층 가서 식사하실분은 따로 리스트 만들기
floor_10 = input('10층 갈 사람: ')
# 명수가 많지 않을 것 같아서 따로 조편성 X
# print(f'10층: {floor_10}') 입력받는게 떠서... 굳이..?
lst_10 = floor_10.split()
for i in lst_10:
    if i in students:
        students.remove(i)

s = set(students) # pop을 쓰기 위해 set으로 형변환
len_s = len(s) % 4
# 대충 5명, 4명조로 나눠봤습니다
for i in range(len(s) % 4): # 출석한 사람 수를 4로 나눈 나머지만큼 5명조 만들기
    lunchmate = []
    for _ in range(5):
        lunchmate.append(s.pop())
    team = ', '.join(lunchmate)
    print(f'20층 {i+1}조: {team}')

for i in range(len(s) // 4): # 남은 인원들로 4명조 만들기
    lunchmate = []
    for _ in range(4):
        lunchmate.append(s.pop())
    team = ', '.join(lunchmate)
    print(f'20층 {len_s + i + 1}조: {team}')

print('점심 맛있게 드세요~~')