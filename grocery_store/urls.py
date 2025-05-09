"""
URL configuration for grocery_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    # request 객체를 받아서 즉시 home.html로 렌더링 / 별도 함수 없이 홈으로 이동하기 위한 템플릿을 바로 렌더링 하기 위해 람다함수 사용 / 람다함수는 간단한 뷰를 빠르게 정의가능한 익명함수
    path('', lambda request: render(request, 'home.html'), name='home'),  # 메인 홈 페이지
    path('admin/', admin.site.urls),
    # 아래의 각 경로로 들어오는 요청은 각각의 앱의 urls.py로 넘겨서 처리
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
]


# 각 앱의 url을 include로 묶음
# 홈화면 및 각 앱의 url들을 적절히 연결하는 메인 url
