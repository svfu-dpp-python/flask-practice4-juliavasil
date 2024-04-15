from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin()

class StudentModelView(ModelView):
    pass

class GroupModelView(ModelView):
    pass