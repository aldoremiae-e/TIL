# 0311 branch



git branch -  독립적인 가상환경 , 원본을 유지한채로 사용이 가능하다.

git init 하면 master (branch)가 나옴 : 빠르고 가볍다.

master branch : 실제로 사용을 하는 가지



## 조회

git branch : 브랜치 목록 확인

## 생성

git branch 이름 : 새로운 브랜치 생성

## 삭제햣ㅈ

git branch -d 이름 : 특정 브랜치 삭제

git branch -D 이름 : 강제 삭제

## 이동

git switch 이름 : 다른 브랜치로 이동

git switch -c 이름 : 브랜치를 새로 생성과 동시에 이동



## 주의사항

버전관리를 받고있는지 아닌지??? 이게머징????



## merge(병합)

git merge 병합할 브랜치 이름

- merge 하기 전에 일단 다른 브랜치를 합치려고하는 즉,  메인 브랜치를 switch해야함