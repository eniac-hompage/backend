from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.shortcuts import reverse
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from config import settings



# Create your models here.
class User(AbstractUser): 
    GENRE_WEB = "WEB"
    GENRE_APP = "APP"
    GENRE_AI = "AI"
    GENRE_GAME = "GAME"
    GENRE_OTHER = "OTHER"

    GENRE_CHOICES = (
      (GENRE_WEB, "WEB"),
      (GENRE_APP, "APP"),
      (GENRE_AI, "AI"),
      (GENRE_GAME, "GAME"),
      (GENRE_OTHER, "OTHER")
    )
    username = models.CharField(max_length=20, blank=True, null=True, verbose_name='유저이름')
    major = models.CharField(max_length=20, blank=True, null=True, verbose_name='전공')
    git_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='깃허브주소')
    eniac_code = models.CharField(max_length=20, null=True, blank=True, verbose_name='')
    entered_eniac = models.SmallIntegerField(default=32, max_length=10, verbose_name='에니악기수')
    fav_pro_genre = models.CharField(max_length=20, blank=True, null=True, verbose_name='선호장르')
    blog_url = models.URLField(default=32, max_length=200, verbose_name='블로그주소')

    student_id = models.IntegerField( max_length=20, blank=True, null=True, verbose_name='학번')
    phone_number = models.CharField(max_length=40, blank=True, null=True, verbose_name='전화번호')
    
    email_confirmed = models.BooleanField(default=False, verbose_name='이메일인증')
    email_secret = models.CharField(max_length=120, default="", blank=True, verbose_name='유저이름')

    email = models.CharField(max_length=80, default="", blank=True, verbose_name='이메일')


    def get_absolute_url(self):
        return reverse("user:profile", kwargs={'pk': self.pk})

    def verify_email(self):
        if self.email_confirmed is False:
            secret = uuid.uuid4().hex[:30]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "에니악 인증호가인",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                html_message=html_message,
            )

            self.save()
        return

    def verify_password(self):
        if self.email_confirmed is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "users/password_reset.html", {"secret": secret}
            )
            send_mail(
                "에니악 인증호가인",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                html_message=html_message,
            )

            self.save()
        return

   
