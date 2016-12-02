COUNT = 0 # Global variable maintains a running total of students created.

class myClass():

    """ myClass allows you to create student objects that have both an age
        and a name. COUNT variable is incremented to mantain a running
        total of students."""

    def __init__(self,name,age):
        """ Creates student objects and keeps a running total."""
        self.name = name
        self.age = age
        global COUNT
        COUNT +=1

    def getName(self):
        """Self explanatory."""
        return self.name

    def getAge(self):
        """Self explanatory."""
        return self.age

    def printDetails(self):
        """ Prints student details along with running total of students."""
        print("Name: " + str(self.getName())
              + "\n"
              + "Age: "
              + str(self.getAge())
              + "\n"
              + "Count: "
              + str(COUNT))

    def __str__(self):
        return "This class is great!"



        
