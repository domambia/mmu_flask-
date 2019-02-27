from flask import Flask 

app = Flask(__name__)
#Separations of Concern 

app.config["SECRET_KEY"] = "tjos osasdas"
app.config['SQLACHEMY_DATABASE_URL'] = ""

@app.route("/") # view
def index():
    return "Hellow"

if __name__ == "__main__":
    app.run(debug=True)
