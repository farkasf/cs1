from flask import Flask, request, make_response
import html

app = Flask(__name__)

page_header = """
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="static/styles.css" />
  </head>
  <body id="level1">
    <img src="static/image.jpg">
      <div>
"""

page_footer = """
      </div>
    </body>
</html>
"""

main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" placeholder="search...">
  <input id="button" type="submit" value="Search">
</form>
"""

@app.route("/", methods=["GET"])
def main_page():
    headers = {"X-XSS-Protection": "0"}

    query = request.args.get('query')
    if not query:
        content = page_header + main_page_markup + page_footer
    else:
        unsafe_message = f"No results were found for '<b>{query}</b>'.<br><br>"
        unsafe_message += "<a href='/'>Try again</a>"

        safe_display = f"<p><b>Query Entered:</b> {html.escape(query)}</p><br>"

        content = page_header + safe_display + unsafe_message + page_footer

    response = make_response(content)
    response.headers.update(headers)

    response.set_cookie("session", "AKIAIOSFODNN7EXAMPLE")

    return response

if __name__ == "__main__":
    app.run(debug=True)
