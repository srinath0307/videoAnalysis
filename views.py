from django.shortcuts import render

# Create your views here.

def loginpage(request):
    return render(request,"salary_database/index.html")


def admin_page(request):
    return render(request,"salary_database/loginpage.html",{"user":" (admin)"})

def employee_page(request):
    return render(request, "salary_database/loginpage.html" ,{"user":" (employee)"})
