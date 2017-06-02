from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
import datetime
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Account(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)
    starting_balance = Column(Float, nullable=False)
    current_balance = Column(Float, nullable=False)
    accrued_interest = Column(Float, nullable=False)

    def __repr__(self):
        return self.name

    def account_value(self, value_date = datetime.datetime.now()):
        """
        Find the acounts total value on date or current
        :param value_date: date to calculate the account value
        :return: value
        """

        return None


class Transaction(Model):
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    account = relationship("Account")
    name = Column(String(50), unique = False, nullable=False)
    value = Column(Float, nullable=False)

    def __repr__(self):
        return "{0}:{1}:{2}:{3}".format(self.name, self.value, self.account, self.id)

    def remove_transaction(self):
        """
        Remove the transaction and update the account value
        :return:
        """

        return False