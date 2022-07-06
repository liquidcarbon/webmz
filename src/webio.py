# src/webio.py



from pathlib import Path
from pyodide import JsException
from pyodide.http import pyfetch

async def pyfetch_download(url, filename=None):
    """

    Notes
    -----
    If the word asyncio appears anywhere in your code, including in a comment,
    then PyScript will run Python asynchronously using Pyodide’s .runPythonAsync() method.
    Otherwise, it’ll call the synchronous .runPython() counterpart,
    which doesn’t let you use the await keyword.
    """

    filename = filename or Path(url).name
    try:
        response = await pyfetch(url)
        if response.ok:
            with open(filename, mode="wb") as file:
                file.write(await response.bytes())
    except JsException:
        return None
    else:
        return filename