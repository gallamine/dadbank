from flask import render_template
import logging
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from .models import Account, Transaction

log = logging.getLogger(__name__)


"""
    Application wide 404 error handler
"""
class TransactionModelView(ModelView):
    datamodel = SQLAInterface(Transaction)
    list_columns = ['id', 'account_id', 'account', 'name', 'value']

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


