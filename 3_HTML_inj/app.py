from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)
posts = []

@app.after_request
def add_xss_protection_header(response):
    response.headers["X-XSS-Protection"] = "0"
    return response

@app.route("/")
def index():
    response = make_response(render_template("index.html"))
    response.set_cookie("session", "AKIAIOSFODNN7EXAMPLE")
    return response

@app.route("/get_posts", methods=["GET"])
def get_posts():
    return jsonify({"posts": posts})

@app.route("/add_post", methods=["POST"])
def add_post():
    data = request.get_json()
    content = data.get("content")
    if content:
        posts.append(content)
        return jsonify({"success": True}), 201
    return jsonify({"success": False}), 400

if __name__ == "__main__":
    app.run(debug=True)
