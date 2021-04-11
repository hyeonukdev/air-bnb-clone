from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
# 위와 아래는 동일한 의미
# admin 패널에 등록하기 위해 decorate를 사용
# admin.site.register(models.User, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):

    # 기존꺼에 추가로 합하려면 이렇게
    # # admin panel에 목록을 한 번에 보기 위해
    # list_display = ('username', 'gender', 'language', 'currency', 'superhost')
    # # admin panel에서 filter를 추가하기 위해
    # list_filter = ('language', 'currency', 'superhost')

    # 필드를 커스터마이징하려면 이렇게
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )