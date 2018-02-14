from smsfalcon.db import Base, engine


Base.metadata.create_all(engine)
