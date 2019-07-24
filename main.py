# the import section
import webapp2
import jinja2
import os
import datetime


# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class Main(webapp2.RequestHandler):
	def get(self): 
		main_template = the_jinja_env.get_template('templates/homepage.html')
		self.response.write(main_template.render())
		self.response.write('I am sorry Jon')

class Login(webapp2.RequestHandler):
	def get(self):
		login_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())

class Signup(webapp2.RequestHandler):
	def get(self):
		self.response.write()
class Dashboard(webapp2.RequestHandler):
	def get(self):
		self.response.write()

# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', Main),
  ('/login', Login),
  ('/signup', Signup),
  ('/dashboard', Dashboard),
  ], debug=True)