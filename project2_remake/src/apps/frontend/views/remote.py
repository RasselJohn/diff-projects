from aiohttp import web

from src.apps.frontend.utils import generate_remote_data


class RemoteView(web.View):
    async def get(self):
        params = self.request.query.getall('params')
        items = [params[i:i + 2] for i in range(0, len(params), 2)]

        if not items:
            return web.json_response({'data': []})

        return web.json_response({'data': [*generate_remote_data(*items)]})
