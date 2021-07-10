from django.views.generic import TemplateView

HPEPPER_URL = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
HPEPPER_KEY = "e5e10639377f64cf" # 取得したAPIキー

class IndexView(TemplateView):
    template_name = 'foodie/index.html'