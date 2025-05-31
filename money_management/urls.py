from django.contrib import admin
from django.urls import path
from budget_management.views.category import CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

base_urls = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

router = DefaultRouter()
router.register(r'api/v1/categories/', CategoryViewSet, basename='category')


urlpatterns = router.urls + base_urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # create new category
#     # edit specific category
#     # delete specific category
#     # get list of categories
#     path(r'categories/', CategoryApiView.as_view), 
#     # search for specific category based on text
    
#     # create new sub-category for specific category
#     # get list of sub-categories for specific category
#     path('sub-categories/',),
#     path('categories/search',),

#     # create new transaction
#     # get all of transactions in specific time range
#     path('transactions/'),

#     # get report of money spending
#     path('report/'),
# ]
