import os
import re
from setuptools import setup


def read(f):

    with open(os.path.join(os.path.dirname(__file__), f)) as fin:

        return fin.read().strip()

try:

    version = re.findall(r"""^__version__ = "([^"]+)"\r?$""",
                         read("aiotelegram.py"), re.M)[0]

except IndexError:

    raise RuntimeError("Unable to determine version.")


setup(
    name="aiotelegram",
    version=version,
    description="Tiny asyncio-based telgram api wrapper library",
    long_description=read("readme-pypi.rst"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    author="pohmelie",
    author_email="multisosnooley@gmail.com",
    url="https://github.com/pohmelie/aiotelegram",
    license="WTFPL",
    py_modules=["aiotelegram"],
    install_requires=["aiohttp"],
)
