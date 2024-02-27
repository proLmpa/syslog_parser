from flask import Flask, render_template;
from syslogParser import syslog_parser;

app = Flask(__name__)

@app.route('/')
def syslog():
    return render_template('index.html', logs = syslog_parser())

if __name__ == '__main__':
    app.run()