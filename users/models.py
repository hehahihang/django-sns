from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from posts.models import Post

class Profile(models.Model):
    # 유저를 1:1 연결, 기존 USER 모델에 손상을 주지 않으면서 새로운 필드를 추가하기 위해서 1:1
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #기존 유저 클래스에 없는 image와 info추가
    image = models.ImageField(upload_to='images/', default="image/default.png")
    info = models.TextField(null=True, blank=True)
    
    followings = models.ManyToManyField("self", related_name='followers', symmetrical=False)
    #내가 팔로우하면 자동으로 상대방도 팔로우 하게 된다.(ManyToMany)

# 유저를 생성할떄 profile을 수정하도록 하겠다.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
#sender == receiver에서 설정한 User모델
#instance == 가입하거나 저장한 User의 객체
#created == 현재 새롭게 가입한 회원인지 확인하는 boolean 값
#**kwargs == 함수에서 딕셔너리 형태의 데이터를 사용할 수 있도록 해준다.

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
