from flask import Flask, request, Response
from object import tester

app = Flask(__name__)


@app.route('/xml', methods=['GET'], strict_slashes=False)
def get_xml():

    return Response(tester(), mimetype='application/xml')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
