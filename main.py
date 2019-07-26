# the import section
import webapp2
import jinja2
import os
import datetime
from planner_models import User, Reminders, Events
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

#global variables
date=None
time=None
info=None

dash_dict = {
		'date': str(datetime.date.today().strftime("%d"))+" "+str(datetime.date.today().strftime("%B"))+" "+str(datetime.date.today().strftime("%Y"))
		}








# the handler section
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
		user=getCurrentUser(self)
		if isLoggedIn(self):
			dashboard_template = the_jinja_env.get_template('templates/dashboard.html')
			self.response.write(dashboard_template.render(dash_dict))
		else:
			home_page_template=the_jinja_env.get_template('templates/homepage.html')
			self.response.write(home_page_template.render())

class Login(BaseHandler):
	def get(self):
		login_template  = the_jinja_env.get_template('templates/login.html')
		self.response.write(login_template.render())

		

class Signup(BaseHandler):
	def get(self):
		signup_template = the_jinja_env.get_template('templates/signup.html')
		self.response.write(signup_template.render())


class Dashboard(BaseHandler):
	def get(self):
		user=getCurrentUser(self)
		
		dash_template = the_jinja_env.get_template('templates/dashboard.html')
		if user is not None:
			self.response.write(dash_template.render(dash_dict))
		else:
			self.redirect('/')
	
	def post(self):
		dash_template =  the_jinja_env.get_template('templates/dashboard.html')
		login_template =  the_jinja_env.get_template('templates/login.html')
		username  = self.request.get('username')
		password  = self.request.get('password')
		query=User.query().fetch()
		user = getCurrentUser(self)

		for element  in  query:
			if (element.username  ==  username) and  (element.password == password):
				
				login(self, username)
				self.response.write(dash_template.render(dash_dict))
				break
		if not(isLoggedIn(self)):
			self.response.write(login_template.render())





class Reminders(BaseHandler):
	def get(self):
		user = getCurrentUser(self)
		if user is not None:
			reminders_template=the_jinja_env.get_template('templates/reminders.html')
			self.response.write(reminders_template.render())
		else:
			self.redirect('/')
	def post(self):
		reminders_template=the_jinja_env.get_template('templates/reminders.html')
		date_input = self.request.get('reminder-date')
		info_input = self.request.get('reminder-info')	
		
		#Lets user add reminder
		addreminder = Reminders(info=info_input, date=date_input)
		addreminder.put()
		query = Reminders.query().fetch()
		#Displays all reminders

		reminders_template=the_jinja_env.get_template('templates/reminders.html')
		self.response.write(reminders_template.render({'remind_list': query}))


class Calendar(BaseHandler):
	def get(self):
		user = getCurrentUser(self)
		if user is not None:
			calendar_template=the_jinja_env.get_template('templates/calendar.html')
			self.response.write(calendar_template.render())
		else:
			self.redirect('/')

	def post(self):
		date=self.request.get('date')
		time=self.request.get('event-time')
		info=self.request.get('event-info')
	

		newEvent=Events(date=date,time=time,info=info)
		newEvent.put()
		
		calendar_template=the_jinja_env.get_template('templates/calendar.html')
		#self.redirect('/dashboard')
		self.response.write(calendar_template.render())



class Logout(BaseHandler):
	def get(self):
		logout(self)
		user=getCurrentUser(self)
		if user is not None:
			dash_template=the_jinja_env.get_template('templates/dashboard.html')
		else:
			home_page_template=the_jinja_env.get_template('templates/homepage.html')
			self.response.write(home_page_template.render())

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'your-super-secret-key'
}


class Display(BaseHandler):
	def post(self):
		event_date=self.request.get("cellId")
		query=Events.query().filter(Events.date==date).fetch()
		event_info=None
		event_time=None
		for i in query:
			event_info=i.info
			event_time=i.time
			
		calendar_template=the_jinja_env.get_template('templates/calendar.html')
		self.response.write(calendar_template.render({'date':event_date,'info':event_info, 'time':event_time}))




# the app configuration section	
app = webapp2.WSGIApplication([
		#('/', MainPage),
		('/', Main),
		('/login', Login),
		('/dashboard', Dashboard),
		('/reminders',Reminders),
		('/sign-up', Signup),
		('/calendar',Calendar),
		('/logout',Logout),
		('/displayEvents',Display)
		], debug=True, config=config)
