from flask import Flask
from flask import render_template, make_response, url_for, redirect, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/hosting')
def hosting():
    return render_template('hosting.html', active="hosting")


@app.route('/django-python-web-development')
def webdev():
    return render_template('solutions.html', active="webdev")


@app.route('/our-clients')
def projects():
    return render_template('projects.html', active="projects")


@app.route('/about')
def about():
    return render_template('about.html', active="about")


@app.route('/contact')
def contact():
    return render_template('contact.html', active="contact")


@app.route('/terms-of-use-and-privacy-policy')
def legal():
    return render_template('legal.html')


@app.route('/robots.txt')
def robotstxt():
    response = make_response(render_template("robots.txt"))
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.route("/sitemap.xml")
def sitemap_xml():
    response = make_response(render_template("sitemap.xml"))
    response.headers['Content-Type'] = 'application/xml'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


# Billing redirects
@app.route('/billing/')
@app.route('/billing/<path:url>')
def billing_redirect(url=""):
    billing_chunks = request.url.split('/billing', 2)
    url = ""
    if len(billing_chunks) == 2:
        url = billing_chunks[1]

    return redirect("https://billing.silvers.net" + str(url))


# Legacy PHP redirect URLs
@app.route('/index.php')
def old_index_redirect():
    return redirect(url_for('home'))


@app.route('/contact.php')
def old_contact_redirect():
    return redirect(url_for('contact'))


@app.route('/hosting.php')
def old_hosting_redirect():
    return redirect(url_for('hosting'))


@app.route('/about.php')
def old_about_redirect():
    return redirect(url_for('about'))


@app.route('/legal.php')
def old_legal_redirect():
    return redirect(url_for('legal'))
