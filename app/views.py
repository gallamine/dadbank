from flask import render_template
import logging
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from .models import Account, Transaction
import datetime
from wtforms import ValidationError

log = logging.getLogger(__name__)


class PastDateCheck(object):
    """
    Verify the Date passed into the form is <= to today
    """
    def __init__(self, now_date=None, message=None):
        if now_date:
            self.now_date = now_date
        else:
            self.now_date = datetime.date.today()

        if not message:
            message = u'Datetime must be less or equal to {}.'.format(self.now_date)
        self.message = message

    def __call__(self, form, field):
        if field.data > self.now_date:
            raise ValidationError(self.message)



"""
    Application wide 404 error handler
"""
class TransactionModelView(ModelView):
    datamodel = SQLAInterface(Transaction)
    list_columns = ['id', 'account', 'date', 'name', 'value']

    validators_columns = {'date': [PastDateCheck()]
                          }

class AccountModelView(ModelView):
    datamodel = SQLAInterface(Account)
    related_views = [TransactionModelView]
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'



class AccountValueView(ModelView):
    datamodel = SQLAInterface(Transaction)

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

appbuilder.add_view(AccountModelView, "List Accounts", icon="fa-folder-open-o", category="Account")
appbuilder.add_view(TransactionModelView, "List Transactions")


