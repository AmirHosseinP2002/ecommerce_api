from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from . import views


router = DefaultRouter()

router.register('products', views.ProductViewSet, basename='product')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('carts', views.CartViewSet, basename='cart')
router.register('orders', views.OrderViewSet, basename='order')
router.register('customers', views.CustomerViewSet, basename='customer')

products_router = NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('comments', views.CommentViewSet, basename='product-comments')
products_router.register('images', views.ProductImageViewSet, basename='product-images')

carts_router = NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + products_router.urls + carts_router.urls
