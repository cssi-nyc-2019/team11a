# the import section
import webapp2
import jinja2
import os
import datetime
from planner_models import User
from webapp2_extras import sessions


# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

# other functions should go above the handlers or in a separate file

def getCurrentUser(self):
	#will return None if user does not exist
	return self.session.get('user')

def login(self, id):
	self.session['user'] = id

def logout(self):
	self.session['user'] = None

def isLoggedIn(self):
	if self.session['user'] is not None:
		return True
	else:
		return False


class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()




# the handler section
class Main(BaseHandler):
	def get(self): 
		main_template = the_jinja_env.get_template('templates/homepage.html')
		self.response.write(main_template.render())
		logout(self)

class Login(BaseHandler):
	def get(self):
		login_template  = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())

	def post(self):
		dash_template =  the_jinja_env.get_template('templates/dashboard.html')
		logg_template =  the_jinja_env.get_template('templates/login.html')
		username  = self.request.get('username')
		password  = self.request.get('password')
		query=User.query().fetch()
		loggedIn=False

		for element  in  query:
			if (element.username  ==  username) and  (element.password == password):
				self.response.write(dash_template.render())
				loggedIn=True
				break
		if  loggedIn==False:
			self.response.write(logg_template.render())

		

class Signup(BaseHandler):
	def get(self):
		signup_template = the_jinja_env.get_template('templates/signup.html')
		self.response.write(signup_template.render())
	def post(self):
		email = self.request.get('email')
		username = self.request.get('username')
		password = self.request.get('password')

		user = User(email=email, username=username, password=password)
		user.put()
		login(self, username)
		log_template = the_jinja_env.get_template('templates/login.html')
		self.response.write(log_template.render())

class Dashboard(BaseHandler):
	def get(self):
<<<<<<< HEAD
		user = getCurrentUser(self)
		if user is not None:
			dash_template = the_jinja_env.get_template('templates/dashboard.html')
			self.response.write(dash_template.render())
		else:
			self.redirect('/')
=======
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

>>>>>>> 937a3706d4052559b354f706395fecd286c12ed4

class Reminders(BaseHandler):
		def get(self):
			user = getCurrentUser(self)
			if user is not None:
				reminders_template=the_jinja_env.get_template('templates/reminders.html')
				self.response.write(reminders_template.render())
			else:
				self.redirect('/')

class Calendar(BaseHandler):
	def get(self):
		user = getCurrentUser(self)
		if user is not None:
			calendar_template=the_jinja_env.get_template('templates/calendar.html')
			self.response.write(calendar_template.render())
		else:
			self.redirect('/')

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'your-super-secret-key',
}





# the app configuration section	
app = webapp2.WSGIApplication([
		#('/', MainPage),
		('/', Main),
		('/login', Login),
		('/dashboard', Dashboard),
		('/reminders',Reminders),
		('/sign-up', Signup),
		('/calendar',Calendar)
		], debug=True, config=config)
