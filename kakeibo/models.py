from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('食費', '食費'),
        ('交通費', '交通費'),
        ('娯楽費', '娯楽費'),
        ('日用品', '日用品'),
        ('医療費', '医療費'),
        ('その他', 'その他'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # ←ここ修正！！
    amount = models.PositiveIntegerField()
    memo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.date} {self.category} {self.amount}円"
