# Asyncio wait on socket
example of starting socket-based server with asyncio
```
loop = asyncio.get_event_loop()

socket_file = "/tmp/example-server.socket"
if os.path.exists(socket_file):
    os.remove(socket_file)
loop.run_until_complete(
    asyncio.start_unix_server(handler, path=socket_file))
os.chmod(socket_file, 0o666)
loop.run_forever()
# ...
```
(Borrowed from the [python3 asyncio start_unix_server permission](https://stackoverflow.com/questions/52244082/python3-asyncio-start-unix-server-permission)
