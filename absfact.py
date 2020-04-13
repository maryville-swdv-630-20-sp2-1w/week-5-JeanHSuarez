from abc import ABCMeta, abstractmethod

"""
Run python3 on the terminal.
Abstract Factory Pattern -  The Person as a base class for the staff, clubhouse member, admin
employees class. The person factory class creates the children classes. The main function
shows the creation of the instance using the factory class. 
"""

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

def main():
   factory = PersonFactory()
   print (factory.create('staff', 'Sam', 'Club', '123-45-6789', '212-123-0001'))
   print (PersonFactory.create('staff', 'Tracy', 'Chapman', '234-56-6789', '516-234-002')) 

   member = factory.create('member', 'Rona', 'Irus', '098-76-5432', '610-123-0003')
   print (member)

   admin = factory.create('admin', 'Connie','David', '345-20-0987' , '610-145-0004')
   print(admin.get_role())


if __name__== "__main__":
   main()