from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("cart/", views.CartViewSet)
router.register("cart-item/", views.CartItemViewSet)

urlpatterns = router.urls
