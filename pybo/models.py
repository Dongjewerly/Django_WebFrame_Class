from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)  #Question 모델, 질문의 제목
    content = models.TextField() #Question 모델, 질문의 내용
    create_date = models.DateTimeField() #Question 모델, 질문을 작성한 일시
    def __str__(self): #id대신에 제목을 확인하는 함수
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE) #부모와 자식이 foreginkey question으로 연결되어있는데 이를 같이 연쇄 삭제한다.
    content = models.TextField() #Answer모델, 답변의 질문(위에), 답변의 내용
    create_date = models.DateTimeField() #Answer모델, 답변을 작성한 일시 python manage.py shell을 통해서 쉘 접근이 가능함
