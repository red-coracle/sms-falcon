# sms-falcon
SMS/Signal gateway for SMSSync

Still a work in progress.


## Features
* Relay SMS messages to/from Signal network using 
[SMSSync](https://github.com/red-coracle/SMSSync) and [signal-cli](https://github.com/AsamK/signal-cli)
* Simple web interface to send directly
* Built with falcon, sqlalchemy, and gunicorn

## Requirements
* Python 3.6+
* Android phone with SMSSync
* Installed signal-cli

## Installation
* Create and activate virtual environment
* `$ pip install -r requirements.txt`
* `$ cp config-example.py smsfalcon/config.py`
* `$ python create_database.py`
* `$ ./run.sh`
