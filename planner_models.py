from google.appengine.ext import ndb

class User(ndb.Model):
	email = ndb.StringProperty(required=True)
	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)


class Events(ndb.Model):
	date = ndb.StringProperty(required=True)
<<<<<<< HEAD
	time = ndb.StringProperty(required=True)
=======
	time = ndb.IntegerProperty(required=True)
<<<<<<< HEAD
=======
>>>>>>> 7e426f1c0ef346b0b9ca8f78200ad8ed25c5ea53
	info = ndb.StringProperty(required=True)
>>>>>>> b9cce9634ba6ff969921c6f361859ad8ce54548e


class Reminders(ndb.Model):
	info = ndb.StringProperty(required=True)
	date = ndb.StringProperty(required=True)