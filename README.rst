This project tries to reproduce an error with websocket
connections.


  uvicorn uvicorn_exception.asgi:application


starts the Django project.

Connecting from a browser's JavaScript konsole:

  c = new WebSocket("ws://localhost/ws/foo/")

is successful and prints "accepting". A connection to

  c = new WebSocket("ws://localhost/ws/bar/")

prints "not accepting => return" and doesn't get accepted.
But I get exception tracebacks. First when closing the
websocket by closing the browser, for example, or loading a
new url, and then after Ctrl+c to stop uvicorn.

  [2020-05-28 15:40:12 +0000] [4621] [INFO] Listening at: http://0.0.0.0:8989 (4621)
  [2020-05-28 15:40:12 +0000] [4621] [INFO] Using worker: uvicorn.workers.UvicornWorker
  [2020-05-28 15:40:12 +0000] [4624] [INFO] Booting worker with pid: 4624
  [2020-05-28 15:40:12 +0000] [4624] [INFO] Started server process [4624]
  [2020-05-28 15:40:12 +0000] [4624] [INFO] Waiting for application startup.
  [2020-05-28 15:40:12 +0000] [4624] [INFO] ASGI 'lifespan' protocol appears unsupported.
  [2020-05-28 15:40:12 +0000] [4624] [INFO] Application startup complete.


  accepting
  not accepting => return

  [2020-05-28 15:40:31 +0000] [4624] [ERROR] Exception in ASGI application
  Traceback (most recent call last):
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 153, in run_asgi
      result = await self.app(self.scope, self.asgi_receive, self.asgi_send)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/middleware/proxy_headers.py", line 45, in __call__
      return await self.app(scope, receive, send)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/middleware/asgi2.py", line 7, in __call__
      await instance(receive, send)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/channels/consumer.py", line 62, in __call__
      await await_many_dispatch([receive], self.dispatch)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/channels/utils.py", line 58, in await_many_dispatch
      await task
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/channels/utils.py", line 50, in await_many_dispatch
      result = task.result()
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 233, in asgi_receive
      data = await self.recv()
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/websockets/protocol.py", line 495, in recv
      return_when=asyncio.FIRST_COMPLETED,
    File "/usr/lib/python3.7/asyncio/tasks.py", line 361, in wait
      fs = {ensure_future(f, loop=loop) for f in set(fs)}
    File "/usr/lib/python3.7/asyncio/tasks.py", line 361, in <setcomp>
      fs = {ensure_future(f, loop=loop) for f in set(fs)}
    File "/usr/lib/python3.7/asyncio/tasks.py", line 592, in ensure_future
      raise TypeError('An asyncio.Future, a coroutine or an awaitable is '
  TypeError: An asyncio.Future, a coroutine or an awaitable is required



  ^C[2020-05-28 15:40:35 +0000] [4621] [INFO] Handling signal: int
  [2020-05-28 15:40:35 +0000] [4624] [INFO] Shutting down
  [2020-05-28 15:40:35 +0000] [4624] [INFO] Error while closing socket [Errno 9] Bad file descriptor
  [2020-05-28 15:40:35 +0000] [4624] [INFO] Finished server process [4624]
  [2020-05-28 15:40:35 +0000] [4624] [INFO] Worker exiting (pid: 4624)
  Task exception was never retrieved
  future: <Task finished coro=<WebSocketProtocol.run_asgi() done, defined at /home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py:147> exception=RuntimeError('unable to perform operation on <TCPTransport closed=True reading=False 0x1a999a8>; the handler is closed')>
  Traceback (most recent call last):
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 153, in run_asgi
      result = await self.app(self.scope, self.asgi_receive, self.asgi_send)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/middleware/proxy_headers.py", line 45, in __call__
      return await self.app(scope, receive, send)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/middleware/asgi2.py", line 7, in __call__
      await instance(receive, send)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/channels/consumer.py", line 62, in __call__
      await await_many_dispatch([receive], self.dispatch)
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/channels/utils.py", line 58, in await_many_dispatch
      await task
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/channels/utils.py", line 50, in await_many_dispatch
      result = task.result()
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 233, in asgi_receive
      data = await self.recv()
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/websockets/protocol.py", line 495, in recv
      return_when=asyncio.FIRST_COMPLETED,
    File "/usr/lib/python3.7/asyncio/tasks.py", line 361, in wait
      fs = {ensure_future(f, loop=loop) for f in set(fs)}
    File "/usr/lib/python3.7/asyncio/tasks.py", line 361, in <setcomp>
      fs = {ensure_future(f, loop=loop) for f in set(fs)}
    File "/usr/lib/python3.7/asyncio/tasks.py", line 592, in ensure_future
      raise TypeError('An asyncio.Future, a coroutine or an awaitable is '
  TypeError: An asyncio.Future, a coroutine or an awaitable is required

  During handling of the above exception, another exception occurred:

  Traceback (most recent call last):
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 159, in run_asgi
      self.send_500_response()
    File "/home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/uvicorn/protocols/websockets/websockets_impl.py", line 136, in send_500_response
      self.transport.write(b"".join(content))
    File "uvloop/handles/stream.pyx", line 673, in uvloop.loop.UVStream.write
    File "uvloop/handles/handle.pyx", line 159, in uvloop.loop.UVHandle._ensure_alive
  RuntimeError: unable to perform operation on <TCPTransport closed=True reading=False 0x1a999a8>; the handler is closed
  Task was destroyed but it is pending!
  task: <Task pending coro=<WebSocketServerProtocol.handler() done, defined at /home/obelisk/.virtualenvs/uvicorn_exception/lib/python3.7/site-packages/websockets/server.py:118> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x7f7e7c7896d8>()]>>
  [2020-05-28 15:40:35 +0000] [4621] [INFO] Shutting down: Master
