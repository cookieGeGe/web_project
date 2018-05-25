from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from app.models import Foodtype,Goods

class MarketRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):

        if renderer_context:

            if isinstance(data, dict):

                msg = data.pop('msg', '请求成功')
                code = data.pop('code', 200)
            else:
                msg = '请求成功'
                code = 200
            rect = {
                'msg': msg,
                'code': code,
                'data': data,
            }
            return super().render(rect, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)