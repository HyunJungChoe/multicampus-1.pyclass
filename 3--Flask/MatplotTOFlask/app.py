import io
import random
from flask import Flask, Response, request

from matplotlib.backends.backend_agg import FigureCanvasAgg

from matplotlib.figure import Figure

app = Flask(__name__)

# @app.route("/")
# def index():
#     num_x_points = int(request.args.get("num_x_points", 50))
#     return render_template("index.html")

@app.route("/")




if __name__ == '__main__':
    app.run()
    