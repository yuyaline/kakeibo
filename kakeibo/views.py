import calendar
from django.shortcuts import render, redirect
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from datetime import date
from django.utils.safestring import mark_safe
from .models import Expense
from django.shortcuts import get_object_or_404


class CustomHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, daily_totals, year, month):
        super().__init__(firstweekday=6)
        self.daily_totals = daily_totals
        self.year = year
        self.month = month

    def formatday(self, day, weekday):
        if day == 0:
            return '<td></td>'  # 日付が無いセル

        total = self.daily_totals.get(day, 0)
        link = f'/day/{self.year}/{self.month}/{day}/'  # ここでリンク作成

        if total > 0:
            return f'<td><a href="{link}"><strong>{day}</strong><br>¥{total}</a></td>'
        else:
            return f'<td><a href="{link}">{day}</a></td>'



@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('calendar')  # 登録後はカレンダー画面にリダイレクト
    else:
        form = ExpenseForm()
    
    return render(request, 'kakeibo/expense_form.html', {'form': form})

@login_required
def calendar_view(request):
    today = date.today()
    year = today.year
    month = today.month

    # 今月の支出データを取得
    expenses = Expense.objects.filter(
        user=request.user,
        date__year=year,
        date__month=month
    )

    # 日付ごとに支出合計をまとめる
    daily_totals = {}
    for expense in expenses:
        day = expense.date.day
        daily_totals[day] = daily_totals.get(day, 0) + expense.amount

    # カレンダーを生成（カスタム）
    cal = CustomHTMLCalendar(daily_totals, year, month)
    html_calendar = cal.formatmonth(year, month)

    context = {
        'year': year,
        'month': month,
        'calendar': mark_safe(html_calendar),
    }
    return render(request, 'kakeibo/calendar.html', context)


@login_required
def day_detail(request, year, month, day):
    selected_date = date(year, month, day)
    expenses = Expense.objects.filter(
        user=request.user,
        date=selected_date
    )

    context = {
        'selected_date': selected_date,
        'expenses': expenses,
    }
    return render(request, 'kakeibo/day_detail.html', context)

@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('day_detail', year=expense.date.year, month=expense.date.month, day=expense.date.day)
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'kakeibo/expense_form.html', {'form': form, 'edit': True})


@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    date_info = (expense.date.year, expense.date.month, expense.date.day)
    expense.delete()
    return redirect('day_detail', year=date_info[0], month=date_info[1], day=date_info[2])
