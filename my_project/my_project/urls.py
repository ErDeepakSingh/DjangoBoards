"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from django.contrib.auth.views import (LoginView,
                                       LogoutView, PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)
from boards.views import (
                          board_topics,
                          new_topic,
                          topic_posts,
                          reply_topic,
                          )

from boards.views import (PostUpdateView,
                          BoardListView,
                          PostListView,
                          UserUpdateView)

from accounts import views as accounts_views

# handler404 = 'boards.views.handler404'
# handler500 = 'boards.views.handler500'

urlpatterns = [

    # path('', home, name='home'),
    path('', BoardListView.as_view(), name='home'),
    path('sign_up/', accounts_views.sign_up, name='signup'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('settings/account/', UserUpdateView.as_view(),name="my_account"),
    path('settings/password/', PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    path('settings/password/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    path('reset/', PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'),
         name='password_reset'),
    path('reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/complete/',
         PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    path('new_topic/<int:id>/', new_topic, name='new_topic'),
    path('boards/<int:id>/', board_topics, name='board_topics'),
    # path('boards/<int:id>/topic/<int:topic_id>/', topic_posts, name='topic_posts'),
    path('boards/<int:id>/topic/<int:topic_id>/', PostListView.as_view(), name='topic_posts'),
    path('boards/<int:id>/topic/<int:topic_id>/reply/', reply_topic, name='reply_topic'),
    path('boards/<int:id>/topic/<int:topic_id>/posts/<int:post_id>/edit/', PostUpdateView.as_view(), name='edit_post'),

    path('admin/', admin.site.urls),
]
