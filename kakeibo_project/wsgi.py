import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kakeibo_project.settings')

# ===== ここから追加 =====
import django
django.setup()
from django.core.management import call_command
call_command('migrate')

from django.contrib.auth import get_user_model

User = get_user_model()

# ここでユーザーがまだいなければ管理者ユーザー作成
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
# ===== ここまで追加 =====

application = get_wsgi_application()
