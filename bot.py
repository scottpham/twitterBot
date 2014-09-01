from flask import Flask, render_template, request, redirect, url_for
import tweet

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def tweet_data():
    body = request.json
    tweet_list = body['tweetDict']
    tweet.tweet(tweet_list)
    return redirect(url_for("index"))

@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
