from app import db
import datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    cost = db.Column(db.Float, nullable=False)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Float, nullable=False)


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    type = db.Column(db.String(50), nullable=False) # 'in' for income or 'out' for outcome
    items = db.relationship('InvoiceItem', backref='invoice')


class InvoiceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    quantity = db.Column(db.Integer, default=0)
    cost = db.Column(db.Float, nullable=False)


