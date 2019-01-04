import json
import socketio


class Alerts:
    def __init__(self):
        socket_token = json.load(open("./socket_token.json"))['socket_token']
        URL = f"https://sockets.streamlabs.com?token={socket_token}"
        sio = socketio.Client()

        @sio.on('connect')
        def connect():
            print('Connected')

        @sio.on('event')
        def event(data):
            t = data['type']
            response = "Error"
            if data["for"] == "twitch_account":
                if t == 'donation':
                    response = f'Thanks for the {data["message"][0]["amount"]} dollars {data["message"][0]["name"]}! ' \
                        f'{data["message"][0]["name"]} says {data["message"][0]["message"][0:50]}'
                elif t == 'follow':
                    response = f'Thanks for following {data["message"][0]["name"]}!'
                elif t == 'subscription':
                    response = f'Thanks for subscribing {data["message"][0]["name"]}! Welcome to the team!'
                elif t == 'bits':
                    response = f'Thanks for the {data["message"][0]["amount"]} bits ' \
                        f'{data["message"][0]["name"]}! {data["message"][0]["name"]} says ' \
                        f'{data["message"][0]["comment"][0:50]}'
                elif t == 'host':
                    response = f'Thanks for the host {data["message"][0]["name"]}!'
            elif data["for"] == "youtube_account":
                if t == 'donation':
                    response = f'Thanks for the {data["message"][0]["amount"]} dollars {data["message"][0]["name"]}! ' \
                        f'{data["message"][0]["name"]} says {data["message"][0]["message"][0:50]}'
                elif t == 'follow':
                    response = f'Thanks for subscribing {data["message"][0]["name"]}!'
                elif t == 'subscription':
                    response = f'Thanks for being a member {data["message"][0]["name"]}! Welcome to the team!'
                elif t == 'superchat':
                    response = f'Thanks for the {data["message"][0]["displayString"].replace("$", "").split(".")[0]} ' \
                        f'dollars {data["message"][0]["name"]}! {data["message"][0]["name"]} says ' \
                        f'{data["message"][0]["comment"][0:50]}'
            return response

        sio.connect(URL)
