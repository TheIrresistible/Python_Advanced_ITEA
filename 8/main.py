from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


class ConnManager:

    def __init__(self, db_name):

        self.db_name = db_name

    def __enter__(self):

        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.conn.close()
        if exc_val:
            raise


def give_and_return(sql, *args):
    list_of_smt = []
    with ConnManager('products.db') as conn:
        cursor = conn.cursor()
        products = cursor.execute(sql, [*args])
        for i in products:
            list_of_smt.append(*i)
    return list_of_smt


@app.route('/')
def categories():
    category = give_and_return('SELECT category FROM categories')
    return render_template('index.html', categories=category)


@app.route('/<category_title>')
def product(category_title):
    products = give_and_return('SELECT title FROM product '
                               'INNER JOIN categories '
                               'ON product.category = categories.category_id '
                               'WHERE categories.category = ?', category_title)
    return render_template('products.html', products=products, category=category_title)


@app.route('/<category_title>/<product_title>')
def product_info(category_title, product_title):
    price = give_and_return('SELECT price FROM product '
                            'WHERE title = ?', product_title)
    instock = give_and_return('SELECT instock FROM product '
                              'WHERE title = ?', product_title)
    quantity = give_and_return('SELECT quantity FROM product '
                               'WHERE title = ?', product_title)
    return render_template('product_info.html', title=product_title, price=str(price)[1:-1],
                           instock=str(instock)[2:-2], quantity=str(quantity)[1:-1])


@app.route('/admin', methods=['GET', 'POST'])
def new_data():
    if request.method == 'POST':
        if request.form['category'] == 'Dairy products':
            category = 1
        elif request.form['category'] == 'Fruits and vegetables':
            category = 2
        elif request.form['category'] == 'Cereals':
            category = 3
        elif request.form['category'] == 'Drinks':
            category = 4
        with ConnManager('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO product(title, category, price, instock, quantity) '
                           'VALUES(?, ?, ?, ?, ?)',
                           [request.form['title'], category, request.form['price'], request.form['instock'],
                            request.form['quantity']])
            conn.commit()
        return render_template('admin.html')
    elif request.method == 'GET':
        return render_template('admin.html')


app.run(debug=True)
