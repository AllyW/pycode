from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/user/<username>')
def profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

with app.test_request_context():
    print url_for('profile', username = 'John Doe')

if __name__ == "__main__":
    app.logger.debug('A value for debugging')
    app.run()

