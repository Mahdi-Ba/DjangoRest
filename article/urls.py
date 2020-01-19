from rest_framework import routers
from .viewsets import ArticleViewset,WriterViewset



router = routers.DefaultRouter()
router.register(r'article', ArticleViewset)
router.register(r'writer', WriterViewset)
urlpatterns = router.urls