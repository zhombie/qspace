from sanic import response

from api.base import BaseView


class IndexView(BaseView):

    async def get(self, request):
        return response.text('Hello, world!')
