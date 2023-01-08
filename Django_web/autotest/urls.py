urlpatterns =[
    path("admin/", admin.site.urls),
    path("test/", views.test),
    path("login/", views.login),
    path("home/",views.home)
]
