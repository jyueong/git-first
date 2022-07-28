# 여기에 필요한 모듈을 추가합니다.
import random, json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []


    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(n):
            a = random.sample(range(1, 46), 6)
            a.sort()
            self.number_lines.append(a)
        # return self.number_lines # 일단 저장만

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = self.get_draw_date(draw_number)
        print("================================")
        print(f"         제 {draw_number} 회 로또         ")
        print("================================")
        print(f"추첨일 : {year}/{month}/{day} (토)         ")
        print("================================")
        for i in range(len(self.number_lines)):
            print(f"{chr(65 + i)} : {self.number_lines[i]}")

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        date_json = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        date_list = json.load(date_json)
        year, month, day = date_list['drwNoDate'].split('-')
        return year, month, day


    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        pass
        # return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        pass
        # return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        pass
        # return ranking
