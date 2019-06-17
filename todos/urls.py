from rest_framework import routers

from todos.api.views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet, 'todos')

urlpatterns = router.urls
