import falcon
from .sms import Payload
from .db import Session, SQLAlchemySessionManager


app = falcon.API(middleware=[
    SQLAlchemySessionManager(Session)
])
app.req_options.auto_parse_form_urlencoded = True

payload = Payload()
app.add_route('/sync', payload)
