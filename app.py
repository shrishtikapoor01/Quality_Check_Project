from flask import Flask,render_template,request
import subprocess
from keras.models import load_model

model = load_model("final.h5")

app = Flask("Vine_App")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("form.html")

@app.route("/output",methods=["GET"])
def output():
    fixed_acidity = request.args.get("fixed_acidity")
    volatile_acidity = request.args.get("volatile_acidity")
    citric_acid = request.args.get("citric_acid")
    chlorides = request.args.get("chlorides")
    residual_sugar = request.args.get("residual_sugar")
    free_sulfur_dioxide = request.args.get("free_sulfur_dioxide")
    total_sulfur_dioxide = request.args.get("total_sulfur_dioxide")
    density = request.args.get("density")
    pH = request.args.get("pH")
    sulphates = request.args.get("sulphates")
    alcohol = request.args.get("alcohol")
    ans = model.predict([[float(fixed_acidity), float(volatile_acidity), float(citric_acid), float(residual_sugar),float(chlorides), float(free_sulfur_dioxide),float(total_sulfur_dioxide), float(density),float(pH), float(sulphates), float(alcohol)]])
    ans = ans * 10
    print(ans)
    if ans > 6:
        return render_template('good.html')
    else:
        return render_template('bad.html')


app.run(port=80,debug=True,host='0.0.0.0')
