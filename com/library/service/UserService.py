from com.library.store.UserStore import UserStore


class UserService:
    userStore = UserStore()

    def addUser(self, userList):
        self.userStore.addUser(userList)

    def searchUser(self, userId):
        self.userStore.searchUser(userId)

    def removeUser(self, user):
        self.userStore.removeUser(user)

    def getUser(self, user):
        return self.userStore.getUser(user)
