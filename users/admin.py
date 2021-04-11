from django.contrib import admin
from . import models


@admin.register(models.User)
# 위와 아래는 동일한 의미
# admin 패널에 등록하기 위해 decorate를 사용
# admin.site.register(models.User, CustomUserAdmin)
class CustomUserAdmin(admin.ModelAdmin):

    # admin panel에 목록을 한 번에 보기 위해
    list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    # admin panel에서 filter를 추가하기 위해
    list_filter = ('language', 'currency', 'superhost')