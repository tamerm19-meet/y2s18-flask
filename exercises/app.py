from flask import Flask, render_template
app = Flask(__name__)
like_same_sport = False
@app.route('/')
def home_page():
	players = ["Tamer", "mhmd", "aya", "shiraz"]
	return render_template("index.html", players = players, likes_same_sport = True)



if __name__ == '__main__':
   app.run(debug = True)