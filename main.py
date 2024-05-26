import RPi.GPIO as GPIO
import time
from flask import Flask, request, render_template, jsonify
from flask_bootstrap import Bootstrap
from datetime import datetime

from robotics.servo import set_servo_angle

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set_angle', methods=['POST'])
def set_angle():
    data = request.get_json()
    angle = data.get('angle')
    if angle is not None:
        try:
            set_servo_angle(angle)
            return jsonify({"status": "success", "angle": angle}), 200
        except ValueError as e:
            return jsonify({"status": "error", "message": str(e)}), 400
    return jsonify({"status": "error", "message": "Invalid angle"}), 400


def main():
    try:

        # set_servo_angle(2.5)
        # while True:
            # set_servo_angle(float(input("enter angle: ")))

        app.run(debug=True, port=7005, host="0.0.0.0")


    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()