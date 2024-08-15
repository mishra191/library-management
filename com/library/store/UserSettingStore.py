class UserSettingStore:
    userbooksetting = {}

    def setBookLimitPerUser(self, student_id, maximum):
        self.userbooksetting[student_id] = maximum

    def getBookLimitPerUser(self, student_id):
        return self.userbooksetting[student_id]
