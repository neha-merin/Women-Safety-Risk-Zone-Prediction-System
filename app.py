from flask import Flask, render_template, request
import pandas as pd
import folium
from folium.plugins import HeatMap
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

from flask import Flask, render_template
import pandas as pd
import folium
from folium.plugins import HeatMap

app = Flask(__name__)

@app.route("/")
def home():

    df = pd.read_csv("data.csv")

    m = folium.Map(
        location=[df["Latitude"].mean(), df["Longitude"].mean()],
        zoom_start=13
    )

    heat_data = [
        [row["Latitude"], row["Longitude"], row["Risk_Score"]]
        for _, row in df.iterrows()
    ]

    HeatMap(heat_data).add_to(m)

    m.save("static/heatmap.html")

    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
