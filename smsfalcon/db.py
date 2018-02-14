from .config import SQLALCHEMY_URI, SECRETKEY
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(SQLALCHEMY_URI)
session_factory = sessionmaker(bind=engine)

Session = scoped_session(session_factory)
Base = declarative_base()


class SQLAlchemySessionManager(object):
    def __init__(self, Session):
        self.Session = Session

    def process_resource(self, req, resp, resource, params):
        resource.session = self.Session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            Session.remove()


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    from_ = Column(String)
    message = Column(String)
    message_id = Column(String)
    sent_to = Column(String)
    secret = Column(String)
    device_id = Column(String)
    sent_timestamp = Column(DateTime)
    sent = Column(Boolean)

    @staticmethod
    def request_to_message(parameters, sent=True):
        message = Message(
            from_=parameters['from'],
            message=parameters['message'],
            message_id=parameters['message_id'],
            sent_to=parameters['sent_to'],
            secret=parameters['secret'],
            device_id=parameters['device_id'],
            sent_timestamp=datetime.fromtimestamp(float(parameters['sent_timestamp']) / 1000),
            sent=sent)
        return message

    @validates('secret')
    def validate_secret(self, key, secret):
        # TODO: Replace with real password checking
        assert secret is not None
        assert secret == SECRETKEY
        return secret
