from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", spr = "Karkoli")

@app.route("/calcLove", methods={"POST"})
def calcLove():
    tmp = dict(request.form)
    ime1 = tmp.get("ime1")
    ime2 = tmp.get("ime2")
    if len(ime1)==0 and len(ime2)==0:
        return "0%" 
    
    elif ime1=="Nejc" or ime2=="Nejc":
        return render_template("index.html", rezultat = f"{ime1} + {ime2} = {random.randint(90,100)}%")
    
    elif ime1=="Jan" or ime2=="Jan":
        return render_template("index.html", rezultat = f"{ime1} + {ime2} = {random.randint(0,5)}%" )
    
    r = f"{ime1} + {ime2} = {random.randint(0,100)}%"
    return render_template("index.html", rezulta= r )

app.run(debug= True)

