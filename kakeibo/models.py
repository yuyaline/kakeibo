from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ログインユーザー
    date = models.DateField(auto_now_add=True)                # 登録日（自動で今日）
    category = models.CharField(max_length=50)                # カテゴリ名
    amount = models.PositiveIntegerField()                    # 金額（正の整数）
    memo = models.CharField(max_length=100, blank=True)        # メモ（空でもOK）

    def __str__(self):
        return f"{self.date} {self.category} {self.amount}円"
