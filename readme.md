# aiotelegram
Tiny asyncio-based telgram bot-api wrapper library.

## Reasons
* [aiotg](https://github.com/szastupov/aiotg) is framework, not library and have no proxy support.
* Raw api calls translation is better for understanding and will not break if telegram api will be changed.
* `snake_case`

## Features
* Simple as telegram api is.
* Works with any json provider ([`aiohttp`](https://github.com/KeepSafe/aiohttp) (default), [`aiorequests`](https://github.com/pohmelie/aiorequests), etc.)
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
```python
aiotelegram.Api(token, *, json_getter=None, loop=None, pause=0.05)
```
* token (str): bot-api token
* json_getter (callable): async json provider. Default provider based on `aiohttp`. Example:
```python
async def json_provider(url, *, data, loop):

    # getting json
    return json
```
    * url (str): address to get
    * data (dict): same as `data` for `aiohttp` and `requests`
    * loop (asyncio.BaseEventLoop): event loop to use

* loop (asyncio.BaseEventLoop): loop to use
* pause (int/float): delay between requests in seconds
