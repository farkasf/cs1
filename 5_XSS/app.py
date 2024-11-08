from flask import Flask, render_template, request, make_response

app = Flask(__name__)

class MainPage:
    @staticmethod
    def render_template(filename, context={}):
        return render_template(filename, **context)

    @staticmethod
    @app.route('/', methods=['GET'])
    def get():
        response = make_response()
        response.headers["X-XSS-Protection"] = "0"

        timer = request.args.get('timer', default=None)
        
        if not timer:
            return MainPage.render_template('index.html')
        else:
            return MainPage.render_template('timer.html', {'timer': timer})

if __name__ == '__main__':
    app.run(debug=True)
