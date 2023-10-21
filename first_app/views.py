from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):  #request yazmak zorunlu
    return HttpResponse("bu benim ilk django projem ve ilk indeksim")

# def python_course(request):
#     return HttpResponse("Python Dersleri")

# def java_course(request):
#     return HttpResponse("<h1>Java derslerine hoşgeldiniz</h1>")

#şimdi yukardaki her course için bir fonksiyon yazmak yerine bunu parametrik yapalım 

course_information={
    "python":"Python kursuna hoşgeldiniz ",
    "java":"Java kursuna hoşgeldiniz.",
    "kotlin":"kotlin kursuna hoşgeldiniz",
}
def courses(request,item):
    #return HttpResponse(course_information.get(item,"NOT FOUND!!!")) #dicr özelliğinden faydalandık.
    #return HttpResponse(course_information[item]) bu şekilde de yazılır ama üstündeki kullanımı default değer de tanımlanabilir.
    
    try:
        course=course_information[item]
        return HttpResponse(course)
    except:
        #raise Http404("item doesnt find please choose another course") # burda HTP404 hata kodunda kendi mesajımızı yazdık burada ayrıca gidip settinsçpy sayfasında debug modu False yapıp izin verilen host ip kısmına "127.0.0.1"adresini yazdım.
        return HttpResponseNotFound("Not Found please look for another course") #burada sadece kendi mesajımı gösterebilirim.
def carpmaIslemi(request,s1,s2):
    return HttpResponse(f"{s1} * {s2} = {s1*s2}")



def course_number_view(request,num1):#127.0.0.1/10 --> 127.0.0.1/kotlin
    
   
    course_list=list(course_information.keys())
    try:
        course=course_list[num1] 
        page_to_go=reverse("course",args=[course]) #reverse, course diye bir şey var mı diye bakıyor urllere
        return HttpResponseRedirect(page_to_go) #return HttpResponseRedirect(reverse("course",args=[course])) kullanımı genelde böyledir.

    except:
        return HttpResponseNotFound("Not Found please look for another course")

