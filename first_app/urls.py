from django.urls import path
from .import views

urlpatterns=[
    
    path("",views.index,name="index"), 
    #yukarıdaki işlem adresi http://127.0.0.1:8000/first_app yazınca çalışır

    #path("about",views.index,name="index") #http://127.0.0.1:8000/first_app/about bu adrese girince yapar sadece burasını çalıştırsaydın.
    path("<int:num1>/",views.course_number_view,name="courseNumberView"),
    # path("java/",views.java_course,name="java kursu"),
    #yukarıdaki gidilmesi istenen adresleri tek tek yazmak yerine kullanıcının parametresine göre alacağız
    path("<str:item>/",views.courses,name="course"),# "<str:parameter>/" şeklinde user input alınır.
    path("<int:s1>/<int:s2>/",views.carpmaIslemi,name="carpma"),
    
]