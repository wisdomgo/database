from django.utils.deprecation import MiddlewareMixin
# 中间件
from django.shortcuts import redirect

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, req):
        if req.path_info in ["/login/", "/"]:
            return  # return表示放行
        info = req.session.get("info")
        if info:
            return  # return表示放行
        return redirect("/login/")
