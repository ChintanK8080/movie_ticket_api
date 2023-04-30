from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!',
        }))

    def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get('message')
            date = data.get('date')
            time = data.get('time')
            sender = data.get('sender')

            if message and date and time:
                self.send(text_data=json.dumps({
                    'message': message,
                    'date': date,
                    'time': time,
                    'sender':sender
                }))
            else:
                self.send(text_data=json.dumps({
                    'type': 'error',
                    'message': 'Invalid message format'
                }))
        except json.decoder.JSONDecodeError as e:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': f"Error decoding JSON: {e}"
            }))
