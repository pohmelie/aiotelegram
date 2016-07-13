# aiotelegram
Tiny asyncio-based telgram api wrapper library. Features:
* Simple as telegram api is.
* Based on [`aiohttp`](https://github.com/KeepSafe/aiohttp).
* Proxy available (via [`aiohttp`](https://github.com/KeepSafe/aiohttp) [`ProxyConnector`](http://aiohttp.readthedocs.io/en/stable/client_reference.html#aiohttp.ProxyConnector)).
* `snake_case` api converted to telegram `camelCase`.
* Polling `offset` handled for you via `get_updates` method.
* Source code is [short and simple](https://github.com/pohmelie/aiotelegram/blob/master/aiotelegram.py).

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
