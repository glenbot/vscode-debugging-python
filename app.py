#!/usr/bin/env python
"""
Python Test application
"""
import logging

from aiohttp import web

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def health(request):
    """Handle health check requests from load balancer"""
    return web.Response(text="ok")


async def handle(request):
    """Handle Index"""
    name = request.match_info.get('name', "Anonymous")
    text = f"Hello {name}, welcome to twitch streaming!"
    return web.Response(text=text)


app = web.Application()


app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle),
    web.get('/_health', health)
])


if __name__ == '__main__':
    logger.info('App Starting ..')
    web.run_app(app, port=8888)
