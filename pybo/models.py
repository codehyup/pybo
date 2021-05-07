from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200) # CharField는 최대 글자 개수 설정하고 싶을때 사용 
    content = models.TextField() # TextField는 최대 글자 개수 X
    create_date = models.DateTimeField() # DateTimeField는 시간 관련 속성
    
    def __str__(self):
        return self.subject # 데이터 조회시 id대신 제목을 리턴함

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey로 Question 모델을 연결. on_delete=models.CASCADE는 질문글이 삭제되면 답변글도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()
