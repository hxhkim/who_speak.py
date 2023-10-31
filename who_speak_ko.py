# -*- coding: utf-8 -*-

def who_speaking():
    import random

    members = input("팀원 이름을 띄어쓰기 단위로 입력하세요 (예, 박지성 유재석): ").split()

    random.shuffle(members)
    speaking_member = members[0]

    return speaking_member

result = who_speaking()
print(f"발표자는 {result}입니다.")
