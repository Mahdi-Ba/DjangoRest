from rest_framework import routers
from .viewsets import ArticleViewset



router = routers.DefaultRouter()
router.register(r'article', ArticleViewset)
urlpatterns = router.urls