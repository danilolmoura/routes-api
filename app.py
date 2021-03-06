import os

from application import create_app

port = int(os.environ.get("PORT", 5000))
host = os.environ.get("FLASK_RUN_HOST", '0.0.0.0')

if __name__ == '__main__': 
    app = create_app('dev')
    app.run(host=host, port=port)