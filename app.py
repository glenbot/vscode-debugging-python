#!/usr/bin/env python
"""
Python Test application
"""
from aiohttp import web


async def handle(request):
    """Handle Index"""
    name = request.match_info.get('name', "Anonymous")
    text = f"Hello {name}, welcome to twitch streaming!"
    return web.Response(text=text)


app = web.Application()


app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
])


if __name__ == '__main__':
    web.run_app(app, port=8888)
