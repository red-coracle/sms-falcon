import falcon
from .sms import Payload
from .db import Session, SQLAlchemySessionManager


api = application = falcon.API(middleware=[
    SQLAlchemySessionManager(Session)
])
api.req_options.auto_parse_form_urlencoded = True

payload = Payload()
api.add_route('/sync', payload)
