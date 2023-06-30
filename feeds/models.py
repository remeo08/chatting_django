from django.db import models
from common.models import CommonModel

class Feed(CommonModel):
    title = models.CharField(max_length=120)
    content = models.TextField()

    # user를 지우면 게시글도 지우겠다.
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    # user를 지우면 게시글은 살려 두겠다.
    # user = models.ForeignKey("users.User", on_delete=models.SET_NULL)


# user feed review 
# user 는 여러 개의 feed 작성 가능
# feed 는 하나의 유저만 가능
# 1(user):N(feed) => 부모: user, 자녀: feed(FK) --키는 항상 자녀가 갖는다.
