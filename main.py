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

class Login(webapp2.RequestHandler):
	def get(self):
		login_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())

class Signup(webapp2.RequestHandler):
	def get(self):
		signup_template = the_jinja_env.get_template('templates/signup.html')
		self.response.write(signup_template.render())
class Dashboard(webapp2.RequestHandler):
	def get(self):
		dash_template = the_jinja_env.get_template('templates/dashboard.html')
		self.response.write(dash_template.render())

class Reminders(webapp2.RequestHandler):
  def get(self):
    reminders_template=the_jinja_env.get_template('templates/reminders.html')
    self.response.write(reminders_template.render())

# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', Main),
  ('/login', Login),
  ('/dashboard', Dashboard),
  ('/reminders',Reminders),
  ('/sign-up', Signup)
  ], debug=True)
