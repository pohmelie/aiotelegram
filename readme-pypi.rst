aiotelegram
===========

Tiny asyncio-based telgram bot-api wrapper library.

Reasons
-------

-  `aiotg`_ is framework, not library and have no proxy support.
-  Raw api calls translation is better for understanding and will not
   break if telegram api will be changed.
-  ``snake_case``

Features
--------

-  Simple as telegram api is.
-  Works with any json provider (`aiohttp`_ (default), `aiorequests`_, etc.)
-  ``snake_case`` api converted to telegram ``camelCase``.
-  Polling ``offset`` handled for you via ``get_updates`` method.
-  Handling timeout between requests automatically (via ``pause``
   keyword-only argument).
-  Source code is `short and simple`_.

Installation
------------

::

    python -m pip install aiotelegram

.. _aiotg: https://github.com/szastupov/aiotg
.. _aiohttp: https://github.com/KeepSafe/aiohttp
.. _aiorequests: https://github.com/pohmelie/aiorequests
.. _short and simple: https://github.com/pohmelie/aiotelegram/blob/master/aiotelegram.py
