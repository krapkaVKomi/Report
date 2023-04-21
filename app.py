from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask, render_template, redirect, url_for
from models import *
from forms import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///report.db'
app.secret_key = '1123sklandlk282jsjj'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/product/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, quantity=form.quantity.data, cost=form.cost.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_product.html', form=form)


@app.route('/service/add', methods=['GET', 'POST'])
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(name=form.name.data, cost=form.cost.data)
        db.session.add(service)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_service.html', form=form)


@app.route('/invoice/add', methods=['GET', 'POST'])
def add_invoice():
    #products = Product.query.all()
    #services = Service.query.all()
    form = InvoiceForm()

    if form.validate_on_submit():
        invoice = Invoice(date=form.date.data, type=form.type.data)
        db.session.add(invoice)
        db.session.commit()

        for item in form.items.data:
            product_id = item.get('product')
            service_id = item.get('service')
            quantity = item.get('quantity')
            cost = item.get('cost')

            if product_id:
                product = Product.query.get(product_id)
                invoice_item = InvoiceItem(product=product, quantity=quantity, cost=cost, invoice=invoice)
            else:
                service = Service.query.get(service_id)
                invoice_item = InvoiceItem(service=service, quantity=quantity, cost=cost, invoice=invoice)

            db.session.add(invoice_item)

        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_invoice.html', form=form)#, products=products, services=services)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
