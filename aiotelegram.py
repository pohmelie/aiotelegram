import asyncio
import functools


__version__ = "0.3.1"
version = tuple(map(int, str.split(__version__, ".")))


async def aiohttp_get_json(url, *, data, loop):

    import aiohttp

    async with aiohttp.get(url, data=data, loop=loop) as response:

        return await response.json()


class Api:

    URL = "https://api.telegram.org/bot{token}/{method}"

    def __init__(self, token, *, json_provider=None, loop=None, pause=0.05):

        self.token = token
        self.json_provider = json_provider or aiohttp_get_json
        self.loop = loop or asyncio.get_event_loop()
        self.pause = pause

        self.last_call = self.loop.time()
        self.offset = 0

    async def _api_call(self, method, **options):

        delta = self.pause - (self.loop.time() - self.last_call)
        await asyncio.sleep(max(0, delta), loop=self.loop)

        url = str.format(Api.URL, token=self.token, method=method)
        return await self.json_provider(url, data=options, loop=self.loop)

    def __getattr__(self, method):

        return functools.partial(self._api_call, str.replace(method, "_", ""))

    async def get_updates(self):

        response = await self.getUpdates(offset=self.offset)
        for update in response.get("result", []):

            self.offset = max(self.offset, update["update_id"] + 1)

        return response
