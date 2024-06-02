from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app01 import models
from app01.utils.bootstrap_modelform import BootstrapModelForm
from app01.models import Task
from app01.utils.page_nav import PageNav


class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"


def task_list(request):
    print("1")
    print(request)
    queryset = models.Task.objects.all().order_by("-id")
    page_nav_obj = PageNav(request, queryset)
    page_queryset = page_nav_obj.page_queryset
    page_nav_string = page_nav_obj.get_html()
    form = TaskModelForm()
    content = {"form": form,
               "queryset": page_queryset,
               "page_nav_string": page_nav_string, }
    return render(request, "task/task_list.html", content)


import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # 免除csrf_token认证，就可发post
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    json_string = json.dumps(request.GET)
    return HttpResponse(json_string)


@csrf_exempt  # 免除csrf_token认证，就可发post
def task_add(request):
    print(1)
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))


# def task_edit(req, nid):
#     obj_row = Task.objects.filter(id=nid).first()
#     if req.method == "GET":
#         form = NumModelFormEdit(instance=obj_row)
#         return render(req, "numbers/num_edit.html", {"form": form})
#     form = NumModelFormEdit(instance=obj_row, data=req.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("/numbers/list")
#     return render(req, "numbers/num_edit.html", {"form": form})

def task_delete(req):
    nid = req.GET.get("nid")
    Task.objects.filter(id=nid).delete()
    return redirect("/task/list")

