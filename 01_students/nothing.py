# 여기에 필요한 모듈을 추가합니다.
import random, json

class Lotto:
    year = ''
    month = ''
    day = ''

    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []



    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(n):
            a = random.sample(range(1, 46), 6)
            a.sort()
            self.number_lines.append(a)
        # return self.number_lines

    @staticmethod
    def get_draw_date(draw_number):
        date_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        date_list = json.load(date_json)
        year, month, day = date_list['drwNoDate'].split('-')
        return year, month, day

    def print_number_lines(self, draw_number):
        year, month, day = self.get_draw_date(draw_number)
        print("================================")
        print(f"         제 {draw_number} 회 로또         ")
        print("================================")
        print(f"추첨일 : {year}/{month}/{day} (토)         ")
        print("================================")
        for i in range(len(self.number_lines)):
            print(f"{chr(65 + i)} : {self.number_lines[i]}")

while True:
    n = int(input('생성할 로또 줄 개수를 입력하세요.(1줄에서 5줄까지 생성 가능) : '))
    if n < 1 or n > 5:
        print('1줄에서 5줄까지만 생성 가능합니다. 다시 입력하세요.')
    else:
        break


wow = Lotto()
wow.generate_lines(n)
wow.print_number_lines(1023)