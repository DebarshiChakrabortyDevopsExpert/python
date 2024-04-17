from flask import Flask, render_template
#from deepgram import Deepgram
#from dotenv import load_dotenv
import os
import asyncio
from aiohttp import web
from aiohttp_wsgi import WSGIHandler
from transcript import generate_transcript
from typing import Dict, Callable

app = Flask('aioflask')

@app.route('/')
def index():
    return render_template('index.html')

async def socket(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request) 

    #deepgram_socket = await process_audio(ws)

    while True:
        # data = await ws.receive_bytes()
        # deepgram_socket.send(data)
        socket = await generate_transcript(web.WebSocketResponse)

  

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    aio_app = web.Application()
    wsgi = WSGIHandler(app)
    aio_app.router.add_route('*', '/{path_info: *}', wsgi.handle_request)
    aio_app.router.add_route('GET', '/listen', socket)
    web.run_app(aio_app, port=5555)
