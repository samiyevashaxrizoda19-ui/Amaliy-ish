from flask import Flask
app = Flask(_name_)
app.route("/")
def home():
  return "Salom! Bu registrasiyasiz PaaS amaliy ishi.
  app.run(host="0.0.0.0", port=8080)
