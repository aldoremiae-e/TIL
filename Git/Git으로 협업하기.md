# Git으로 협업하기



## 1. Git branch

```bash
$ git switch -c 브랜치이름
```



## 2. 특정 기능 개발 진행

- frontend는 frontend 작업 환경에서만 진행해야함 - vue.js는 vue.js , django를 건들면 안됨!!
- backend는 backend만!



## 3. 기능 개발 완료 후

```bash
$ git add .
$ git commit -m '커밋 메세지'

$ git push origin 브랜치이름
```



## 4 . GitLab혹은 Github 에서 내가 푸쉬한 내용 `merge / pull request` 누르기



![image-20220524175528032](C:/Users/bamxd/AppData/Roaming/Typora/typora-user-images/image-20220524175528032.png)



## 5.  다른 팀원이 approve 후 merge 눌러야함

- master에 merge가 반영된 상태이다.



## 6. 다른 팀원이 pull 받기

```bash
$ git switch master
$ git pull origin master
```

- 내 로컬에 반영된 프로젝트 받아왔음



## 7. 나는 기존 개발 완료했던 브랜치 삭제

```bash
$ git branch -d 브랜치이름


# master와 관계없이 강제 삭제
$ git branch -D 브랜치이름
```



## 8. 새로운 개발을 하기 위해서는 다시 1번으로

```bash
$ git switch -c 다른브랜치이름
```

