from django.contrib import admin
from django.urls import path, include


# api/v1/feeds GET (조회, 생성)
# api/v1/feeds/id GET (조회, 삭제, 업데이트)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/feeds/', include("feeds.urls")),
    # path('api/v1/reviews/', include("reviews.urls")),
    # path('api/v1/users/', include("users.urls"))

]
