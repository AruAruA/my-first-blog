#他ファイルからなんかもらう（import）
from django.db import models
from django.utils import timezone

# オブジェクト定義
# Post: モデルの名前
# models.Model: ポストがDjango Modelという意味
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # ~.ForeignKey : 他モデルへのリンク
	title = models.CharField(max_length = 200)  # ~.CharField : 文字数制限あるフィールド
	text = models.TextField()                   # ~.TextField : 文字数制限ないフィールド
	created_date = models.DateTimeField(        # ~.DateTimeField : 日付と時間のフィールド
		default = timezone.now)
	published_date = models.DateTimeField(
		blank = True, null = True)

	def publish(self):   # ブログを公開するメソッド（関数定義）
		self.published_date = timezone.now()
		self.save()

	def __str__(self):   # PostのTitleを返す（string型）
		return self.title
