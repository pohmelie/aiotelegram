# aiotelegram
Tiny asyncio-based telgram bot-api wrapper library.

## Reasons
* [aiotg](https://github.com/szastupov/aiotg) is framework, not library and have no proxy support.
* Raw api calls translation is better for understanding and will not break if telegram api will be changed.
* `snake_case`

## Features
* Simple as telegram api is.
* Based on [`aiohttp`](https://github.com/KeepSafe/aiohttp).
* Proxy available (via [`aiohttp`](https://github.com/KeepSafe/aiohttp) [`ProxyConnector`](http://aiohttp.readthedocs.io/en/stable/client_reference.html#aiohttp.ProxyConnector)).
* `snake_case` api converted to telegram `camelCase`.
* Polling `offset` handled for you via `get_updates` method.
* Handling timeout between requests automatically (via `pause` keyword-only argument).
* Source code is [short and simple](https://github.com/pohmelie/aiotelegram/blob/master/aiotelegram.py).

## Installation
```
python -m pip install aiotelegram
```

## Usage
### Polling updates
```python
import aiotelegram


async def ...(...):

    api = aiotelegram.Api(token)
    while True:

        response = await api.get_updates()
        if not response["ok"]:

            ...

        else:

            for update in response["result"]:

                ...

        await asyncio.sleep(delay)
```
### Sending message
```python
async def ...(...):

    await api.send_message(
        chat_id=123456,
        text="*foobar*",
        parse_mode="Markdown",
    )
```
## API
* aiotelegram.Api(token, \*, loop=None, pause=0.05, connector\_factory=lambda **_: None):
    * token (str): bot-api token
    * loop (asyncio.BaseEventLoop): loop to use
    * pause (int/float): delay between requests in seconds
    * connector\_factory (callable): should return aiohttp connector (ProxyConnector, UnixConnector, etc.). connector\_factory get one keyword argument: loop.
