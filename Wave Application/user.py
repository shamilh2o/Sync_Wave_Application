import os


class AppUser:
    def __init__(self, user_id, email):
        self.user_id = user_id
        self.email = email
        self._set_name()
        # self._create_user_dirs(users_dir)
        self.clicks = 0

    def _set_name(self):
        names = self.email.split('@')[0].split('.')
        if len(names) > 1:
            self.first, *_, self.last = names
        elif names:
            self.first = names[0]
            self.last = ''
        self.name = f'{self.first} {self.last}'.strip().title()

