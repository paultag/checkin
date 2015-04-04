import os
import datetime as dt
from flask import Flask, render_template, request

app = Flask(__name__)
TARGET = os.environ.get("CHECKUP_CSV", "/checkup/data.csv")


def respond(message):
    return render_template("sms.xml", message=message)


def save(data):
    when = dt.datetime.utcnow()
    with open(TARGET, 'a') as fd:
        fd.write("{},{}\n".format(when.isoformat(), data))


@app.route('/sms', methods=['POST'])
def sms():
    fro = request.form.get('From', None)
    msg = request.form.get('Body', None)
    try:
        entry = float(msg)
        save(entry)
        return respond("Got it, {}".format(entry))
    except ValueError as e:
        return respond(str(e))
    except Exception as e:
        return respond(str(e))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
