class UserStore:

  def __init__(self):
        self.userstore = {}
  def addUser(self, userList):
     for user in userList:
        self.userstore[user.student_id]= user
     return True

  def removeUser(self, user):
     del  self.userstore[user.student_id]
     return True

  def getUser(self, user):
      if user.student_id in self.userstore:
          return True
      return False

  def searchUser(self, userId):
     return self.userstore[userId]
