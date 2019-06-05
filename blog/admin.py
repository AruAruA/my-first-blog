from django.contrib import admin
from .models import Post  # Postモデルをimport

admin.site.register(Post)    # モデル登録