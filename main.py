# the import section
import webapp2
import jinja2
import os
import datetime
from planner_models import User


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
		login_template  = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())

	
		

class Signup(webapp2.RequestHandler):
	def get(self):
		signup_template = the_jinja_env.get_template('templates/signup.html')
		self.response.write(signup_template.render())
	def post(self):
		email = self.request.get('email')
		username = self.request.get('username')
		password = self.request.get('password')

		user = User(email=email, username=username, password=password)
		print user 
		user.put()
		log_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(log_template.render())

class Dashboard(webapp2.RequestHandler):
	def get(self):
		dash_dict = {
		'date': str(datetime.date.today().strftime("%d"))+" "+str(datetime.date.today().strftime("%B"))+" "+str(datetime.date.today().strftime("%Y"))
		}
		dash_template = the_jinja_env.get_template('templates/dashboard.html')
		self.response.write(dash_template.render(dash_dict))
	def post(self):
		dash_dict = {
		'date': str(datetime.date.today().strftime("%d"))+" "+str(datetime.date.today().strftime("%B"))+" "+str(datetime.date.today().strftime("%Y"))
		}

		dash_template =  the_jinja_env.get_template('templates/dashboard.html')
		logg_template =  the_jinja_env.get_template('templates/login.html')
		username  = self.request.get('username')
		password  = self.request.get('password')
		query=User.query().fetch()
		loggedIn=False

		for element  in  query:
			if (element.username  ==  username) and  (element.password == password):
				self.response.write(dash_template.render(dash_dict))
				loggedIn=True
				break
			 
		if  loggedIn==False:
			self.response.write(logg_template.render())



class Reminders(webapp2.RequestHandler):
		def get(self):
			reminders_template=the_jinja_env.get_template('templates/reminders.html')
			self.response.write(reminders_template.render())

class Calendar(webapp2.RequestHandler):
	def get(self):
		calendar_template=the_jinja_env.get_template('templates/calendar.html')
		self.response.write(calendar_template.render())


# the app configuration section	
app = webapp2.WSGIApplication([
		#('/', MainPage),
		('/', Main),
		('/login', Login),
		('/dashboard', Dashboard),
		('/reminders',Reminders),
		('/sign-up', Signup),
		('/calendar',Calendar)
		], debug=True)
