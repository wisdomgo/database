from django.shortcuts import render, redirect
from django.http import HttpResponse
from app01.models import MyAdmin
from app01.utils.page_nav import PageNav
from app01.srcs.forms.form import MyadminForm, MyadminFormEdit, MyadminFormReset

def myadmin_list(req):
    info = req.session.get("info", {})

    search_data = req.GET.get("q", "")
    search_data_dict = {"user_name__contains": search_data} if search_data else {}
    queryset = MyAdmin.objects.filter(**search_data_dict)
    page_nav_obj = PageNav(req, queryset)
    content = {
        "queryset": page_nav_obj.page_queryset,
        "page_nav_string": page_nav_obj.get_html(),
    }
    return render(req, "myadmin/myadmin_list.html", content)

def myadmin_add(req):
    info = req.session.get("info", {})
    if not info.get("is_superadmin"):
        return HttpResponse("无权访问", status=403)

    if req.method == "GET":
        form = MyadminForm()
        return render(req, "change.html", {"form": form, "add_name": "添加管理员"})
    else:
        form = MyadminForm(data=req.POST)
        if form.is_valid():
            form.save()
            return redirect("/myadmin/list")
        else:
            return render(req, "change.html", {"form": form, "title": "添加管理员"})

def myadmin_edit(req, nid):
    info = req.session.get("info", {})
    if not info.get("is_superadmin"):
        return HttpResponse("无权访问", status=403)

    row_obj = MyAdmin.objects.filter(id=nid).first()
    if not row_obj:
        return render(req, "error.html")

    if req.method == "GET":
        form = MyadminFormEdit(instance=row_obj)
        return render(req, "change.html", {"form": form, "title": "编辑管理员"})
    else:
        form = MyadminFormEdit(instance=row_obj, data=req.POST)
        if form.is_valid():
            form.save()
            return redirect("/myadmin/list")
        return render(req, "change.html", {"form": form, "title": "编辑管理员"})

def myadmin_delete(req):
    info = req.session.get("info", {})
    if not info.get("is_superadmin"):
        return HttpResponse("无权访问", status=403)

    nid = req.GET.get("nid")
    MyAdmin.objects.filter(id=nid).delete()
    return redirect("/myadmin/list")

def myadmin_reset_pwd(req, nid):
    info = req.session.get("info", {})
    if not info.get("is_superadmin"):
        return HttpResponse("无权访问", status=403)

    row_obj = MyAdmin.objects.filter(id=nid).first()
    if not row_obj:
        return render(req, "error.html")

    if req.method == "GET":
        form = MyadminFormReset(instance=row_obj)
        return render(req, "change.html", {"form": form, "title": "重置密码"})
    else:
        form = MyadminFormReset(instance=row_obj, data=req.POST)
        if form.is_valid():
            form.save()
            return redirect("/myadmin/list")
        return render(req, "change.html", {"form": form, "title": "重置密码"})
