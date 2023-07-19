from flask import Flask, abort, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def hello():
    user = {'username': 'John'}
    return render_template('index.html', user=user)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/downloader')
def downloader():
    return render_template('downloader.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


if __name__ == '__main__':
    app.run(debug=True)
