from django.urls import path
from .import views

urlpatterns=[
    #path("",admin.site.urls)#bu şu demek www.benimyazilimcim.com adresine gidilirse
    #path("/contact",views.ornekfonksiyon) #www.benimyazilimcim.com/contact adresi yazılsaydı views içindeki ornekFonksyona gidekcekti
    path("",views.index,name="index"), #bu işlem: first_app içindeki views.py ile urls.py bağlanmış oldu ama asıl urls.py proje içindekine bağlamadım daha
    #yukarıdaki işlem adresi http://127.0.0.1:8000/first_app yazınca çalışır
    #burada first_app kelimesini yazmamı ana projedeki first_app yazmamdan dolayı yani bunun üzerinden git diyorum
    #path("about",views.index,name="index") #http://127.0.0.1:8000/first_app/about bu adrese girince yapar sadece burasını çalıştırsaydın.
    path("<int:num1>/",views.course_number_view,name="courseNumberView"),
    # path("java/",views.java_course,name="java kursu"),
    # path("python",views.python_course,name="python kursu"),
    #yukarıdaki gidilmesi istenen adresleri tek tek yazmak yerine kullanıcının parametresine göre alacağoız
    path("<str:item>/",views.courses,name="course"),# "<str:parameter>/" şeklinde user input alınır.
    path("<int:s1>/<int:s2>/",views.carpmaIslemi,name="carpma"),
    
]