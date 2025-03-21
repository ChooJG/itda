from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # 메인 페이지
    path('product/register/', views.product_register, name='product_register'),  # 상품 등록 페이지
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # 상품 상세 페이지
    path('all-products/', views.all_products, name='all_products'),  # 전체 상품 페이지
    path('popular-products/', views.popular_products, name='popular_products'),  # 인기 상품 페이지
]



from django.conf import settings
from django.conf.urls.static import static


# 개발 환경에서 미디어 파일을 서빙하는 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
