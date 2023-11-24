from rest_framework import routers
from .api import ProjectViewsSet
router = routers.DefaultRouter()

router.register('api/project', ProjectViewsSet, 'project')


urlpatterns = router.urls
