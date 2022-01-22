from datetime import datetime
import json
import logging

import websocket

socket = "wss://stream.bybit.com/realtime"
interval = 10
ping_start = 0


def _prepare_channel_data():
    return {"op": "subscribe", "args": ["klineV2.240.BTCUSD"]}


def _get_ping_payload():
    return json.dumps({'op': 'ping'})


def on_open(ws):
    print(f'Start: {datetime.now()}')

    ws.send(_get_ping_payload())

    channel_data = _prepare_channel_data()

    ws.send(json.dumps(channel_data))


def on_message(ws, message):
    global interval
    global ping_start

    message = json.loads(message)

    print(message)


def _restart_websocket():
    global ws
    global interval

    ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
    ws.run_forever(ping_interval=interval, ping_payload=_get_ping_payload())


def on_close(ws, test1, test2):
    print(f'End: {datetime.now()}')
    print(test1 + '\n---------------\n' + test2)
    print('Restarting Websocket!')
    _restart_websocket()


ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever(ping_interval=interval, ping_payload=_get_ping_payload())
