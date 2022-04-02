from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("dishes/<int:pk>/", views.DishViewSet)
router.register("category/<int:pk>/", views.CategoryViewSet)
router.register("dish_size/", views.DishSizeViewSet)
urlpatterns = router.urls
