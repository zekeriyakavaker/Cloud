import cgi
import datetime
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(
'''<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Cloud Hosting Test</title>
        <link media="all" href="Style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <header>Cloud Hosting Test</header>
        <div id="login">
            <h1>Giriş</h1>
            <form>
                <input type="email" placeholder="Email" />
                <input type="password" placeholder="Şifre" />
                <input type="submit" value="Giriş Yap" />
            </form>
        </div>
    </body>
</html>''')
        
class SignUp(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Üye ol')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/uyeol', SignUp)
], debug=True)
