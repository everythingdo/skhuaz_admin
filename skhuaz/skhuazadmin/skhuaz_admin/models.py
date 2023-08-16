from django.db import models

#User(교수님)
class User(models.Model):
    email = models.CharField(max_length=300) #이메일
    password = models.CharField(max_length=20) #비밀번호
    name = models.CharField(max_length=30) #성함
    phone_number = models.CharField(max_length=20) #전화번호
    department = models.TextField() #소속학과

#강의
class lecture(models.Model) :
    lecture_title = models.CharField(max_length=100) #강의명
    semester = models.IntegerField() #학기
    room = models.CharField(max_length=10) #강의실
    day = models.IntegerField() #강의 요일 [ 0:월, 1:화, 2:수, 3:목, 4:금 ]
    strat_time = models.DateTimeField('date published') #강의 시작 시간
    end_time = models.DateTimeField('date published') #강의 종료 시간
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='professor') #교수님 외래키 연결

#학생이 작성한 후기
class review(models.Model) :
    review_title = models.TextField() #강의평가 제목
    review_content = models.TextField() #강의평가 본문
    review_date = models.DateTimeField('date published') #강의평가 작성일