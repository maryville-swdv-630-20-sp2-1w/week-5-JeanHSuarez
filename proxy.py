from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
   def __init__(self, firstname, lastname, ssn, phonenumber):
      self.firstname = firstname
      self.lastname = lastname
      self.ssn = ssn
      self.phonenumber = phonenumber

   @abstractmethod
   def get_role(self):
         pass

   def __str__(self):
       return "{} - {}, {} with SSN: {}, can be contacted at {} ".format(self.__class__. __name__, 
        self.lastname, self.firstname, self.ssn, self.phonenumber)

class Staff(Person):
   def get_role(self):
      return "staff"

class Member(Person):
   def get_role(self):
      return "member"

class Admin(Person):
   def get_role(self):
      return "admin"

class PersonFactory(object):
   @classmethod
   def create(cls, name, *args):
      name = name.lower().strip()

      if name == 'staff':
         return Staff(*args)
      elif name == 'member':
         return Member(*args)
      elif name == 'admin':
         return Admin(*args)

#Proxy for counting... 

class PersonProxy(object):
# Count of employees
  count = 0

  def __new__(cls, *args):
  # To keep track of counts
    instance = object.__new__(cls)
    cls.incr_count()
    return instance

  def __init__(self, person):
    self.person = person

  @classmethod
  def incr_count(cls):
    """ Increment employee count """
    cls.count += 1

  @classmethod
  def decr_count(cls):
    """ Decrement employee count """
    cls.count -= 1

  @classmethod
  def get_count(cls):
    """" Get employee count """
    return cls.count

  def __str__(self):
    return str(self.person)

  def __getattr__(self, name):
     """ Redirect attributes to employee instance """
     return getattr(self.person, name)

  def __del__(self):
     """ Overloaded __del__ method """
     # Decrement employee count
     self.decr_count()

class PersonProxyFactory(object):
  """ An Employee factory class returning proxy objects """
  @classmethod
  def create(cls, name, *args):
    """ Factory method for creating an Employee instance """
    name = name.lower().strip()
   
    if name == 'staff':
      return PersonProxy(Staff(*args))
    elif name == 'member':
      return PersonProxy(Member(*args))
    elif name == 'admin':
      return PersonProxy(Admin(*args))

def main():

  staff = PersonProxyFactory.create('staff', 'Sam', 'Club', '123-45-6789', '212-123-0001')
  print(staff)

  admin = PersonProxyFactory.create('admin', 'Connie','David', '345-20-0987' , '610-145-0004')

  print(admin.get_count())
  print(PersonProxy.get_count())

  del staff
  print(PersonProxy.get_count())

  del admin
  print(PersonProxy.get_count())

if __name__ == "__main__":

  main()