from django.shortcuts import render, redirect
import datetime


# Create your views here.


def login(request):
    print("COOKIES", request.COOKIES)
    print("SESSION", request.session)

    if request.method == "POST":
        name = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if name == "Aaron" and pwd == "123":
            red = redirect("/index/")
            # red.set_cookie("username", name)
            # red.set_cookie("username", name, max_age=10) # max_age=10 :10秒后cookie失效
            red.set_cookie("username", name, max_age=10, expires=datetime.datetime.utcnow() + datetime.timedelta(
                days=3))  # days=3天后cookie失效，一般这两个时间设置成一样，都可以使cookie失效, session用法也是一样的

            return red

            # COOKIE SESSION
            # request.session["is_login"] = True
            # request.session["user"] = name
            #
            # return redirect("/index/")

    return render(request, "login.html")


def index(request):
    if request.COOKIES.get("username", None) == "Aaron":
        name = request.COOKIES.get("username", None)
        return render(request, "index.html", locals())
    # COOKIE SESSION
    # if request.session.get("is_login", None):
    #
    #     name = request.session.get("user", None)
    #     return render(request, "index.html", locals())

    else:
        return redirect("/login/")
