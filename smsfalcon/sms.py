import io
import json
import falcon
import os
import uuid
from .db import Message
from .config import SECRETKEY
from sqlalchemy.exc import IntegrityError


class Payload(object):
    def __init__(self):
        self.success = True
        self.error = None
        self.required_params = ['from', 'message', 'message_id', 'sent_to',
                                'secret', 'device_id', 'sent_timestamp']

    def on_get(self, req, resp):
        if req.get_param('task') == 'send':
            messages = self.session.query(Message).filter_by(sent=False).count()
            payload = {'payload': {'task': 'send', 'secret': SECRETKEY, 'messages': messages}}
            resp.status = falcon.HTTP_200
            resp.body = payload
        pass

    def on_post(self, req, resp):
        message = Message.request_to_message(req.params)
        try:
            self.session.add(message)
        except IntegrityError as ex:
            self.success = False
            self.error = 'Validation error!'
        if not all(key in req.params for key in self.required_params):
            self.success = False
            self.error = 'Not all params are present'
        if not self.error:
            self.session.commit()
        resp.status = falcon.HTTP_200
        payload = {'payload': {'success': self.success, 'error': self.error}}
        resp.body = json.dumps(payload, ensure_ascii=False)
