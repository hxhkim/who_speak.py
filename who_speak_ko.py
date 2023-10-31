# -*- coding: utf-8 -*-

def who_speaking():
    import random

    members = ["강민정", "김하현", "박수빈", "안인균", "이주선", "심재호"]

    random.shuffle(members)
    speaking_member = members[0]

    return speaking_member

result = who_speaking()
print(result)
