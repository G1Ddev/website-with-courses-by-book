from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from courses.views import CourseListView


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('api/', include('courses.api.urls', namespace='api')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', CourseListView.as_view(), name='course_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)