# who_speak

## DEV
```bash
$ docker run -it --name who_speak -d python:3.12.0-alpine
$ docker ps
CONTAINER ID   IMAGE                  COMMAND     CREATED          STATUS          PORTS     NAMES
bc5f49495b96   python:3.12.0-alpine   "python3"   2 minutes ago    Up 2 minutes              who_speak

$ docker exec -it who_speak sh

/ # ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd home
/home # ls
/home # pwd
/home
/home # mkdir code
/home # ls
code
/home # cd code
/home/code # vi who_speak_ko.py
/home/code # cat who_speak_ko.py
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

def who_speaking():
    import random

    members = input("팀원 이름을 띄어쓰기 단위로 입력하세요 (예, 박지성 유재석): ").split()

    random.shuffle(members)
    speaking_member = members[0]

    return speaking_member

result = who_speaking()
print(f"발표자는 {result}입니다.")

/home/code # python who_speak_ko.py
팀원 이름을 띄어쓰기 단위로 입력하세요 (예, 박지성 유재석):  강민정 김하현 이주선 심재호 안인균 박수빈
발표자는 이주선입니다.
```

## TEST
![image](https://github.com/hxhkim/who_speak/assets/68641751/fdc5e71c-d50f-4593-bce8-6dd8c62eb7c1)

