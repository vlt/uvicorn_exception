from channels.generic.websocket import AsyncWebsocketConsumer


class DefaultConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = self.scope["url_route"]["kwargs"]["token"]

        if token != "foo":
            print("not accepting => return")
            return

        print("accepting")
        await self.accept()
