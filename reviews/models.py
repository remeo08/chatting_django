from django.db import models
from common.models import CommonModel

class Review(CommonModel):
    content = models.CharField(max_length=150)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)

# user review 관계
# user 는 여러 개의 review 작성 가능
# review 는 하나의 user만 가능
# 1(user):N(review) => 부모: user, 자녀: review(FK) --FK키는 항상 자녀가 갖는다.


# feed review 관계
# feed 는 여러 개의 review 작성 가능
# review 는 하나의 feed 만 가능
# 1(feed):N(review) => 부모: feed, 자녀: review(FK) --FK키는 항상 자녀가 갖는다.
