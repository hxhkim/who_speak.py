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

def who_speaking():
    import random

    members = ["강민정", "김하현", "박수빈", "안인균", "이주선", "심재호"]

    random.shuffle(members)
    speaking_member = members[0]

    return speaking_member

result = who_speaking()
print(result)

/home/code # python who_speak_ko.py
심재호
/home/code # python who_speak_ko.py
안인균
/home/code # python who_speak_ko.py
이주선
/home/code # python who_speak_ko.py
김하현
```

## TEST
![image](https://github.com/hxhkim/who_speak/assets/68641751/8391513a-8252-44a8-a58f-7c039e612ce9)
