from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Feed
from .serializers import FeedSerializer


# view.py => serializer를 불러오고, 클라이언트에서 데이터를 받거나, 클라이언트로 데이터를 전달하는 역할

# api/v1/feeds/id GET(조회), POST(생성)
# api/v1/feeds/id GET(조회), DELETE(삭제), PUT(업데이트)

class AllFeed(APIView):
    def get(self, request):
        feeds = Feed.objects.all()

        # objects -> JSON(feeds 폴더에서 serializer 파일 만듦)
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedSerializer(data=request.data)  # 유저가 보낸 데이터(JSON)이라 serializer에 담고 변수명은 serializer로 한다.

        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            return Response('success')
        else:
            return Response(serializer.errors)

# api/v1/feeds/id
class FeedDetail(APIView):
    def get(self, request, feed_id):
        pass

    def put(self, request, feed_id):
        pass

    def delete(self, request, feed_id):
        pass