from google.appengine.ext import ndb

class User(ndb.Model):
	email = ndb.StringProperty(required=True)
	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)


class Events(ndb.Model):
	date = ndb.StringProperty(required=True)

	time = ndb.StringProperty(required=True)

	info = ndb.StringProperty(required=True)



class Reminders(ndb.Model):
	info = ndb.StringProperty(required=True)
	date = ndb.StringProperty(required=True)