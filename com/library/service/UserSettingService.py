from com.library.store.UserSettingStore import UserSettingStore


class UserSettingService:
    userSettingStore = UserSettingStore()

    def setBookLimitPerUser(self, student_id, maximum):
        self.userSettingStore.setBookLimitPerUser(student_id, maximum)

    def getBookLimitPerUser(self, student_id):
        return self.userSettingStore.getBookLimitPerUser(student_id)
