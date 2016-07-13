import asyncio
import functools

import aiohttp


__version__ = "0.1.0"
version = tuple(map(int, str.split(__version__, ".")))


class Api:

    URL = "https://api.telegram.org/bot{token}/{method}"

    def __init__(self, token, *, connector_factory=lambda **_: None,
                 loop=None, pause=0.05):

        self.token = token
        self.connector_factory = connector_factory
        self.pause = pause
        self.loop = loop or asyncio.get_event_loop()
        self.last_call = self.loop.time()
        self.offset = 0

    async def _api_call(self, method, **options):

        now = self.loop.time()
        delta = self.pause - (now - self.last_call)
        await asyncio.sleep(max(0, delta), loop=self.loop)
        self.last_call = now

        request = aiohttp.get(
            str.format(Api.URL, token=self.token, method=method),
            connector=self.connector_factory(loop=self.loop),
            loop=self.loop,
            data=options,
        )
        async with request as response:

            return await response.json()

    def __getattr__(self, method):

        return functools.partial(self._api_call, str.replace(method, "_", ""))

    async def get_updates(self):

        response = await self.getUpdates(offset=self.offset)
        for update in response["result"]:

            self.offset = max(self.offset, update["update_id"] + 1)

        return response
