from datetime import datetime

from flask import Blueprint, session, request, jsonify, render_template

from APP.functions import is_login
from APP.models import House, Order

from utils import status_code

orders = Blueprint('order', __name__)


@orders.route('/', methods=['POST'])
@is_login
def order_com():
    user_id = session['user_id']
    house_dict = request.form
    house_id = house_dict.get('id')
    start_date = house_dict.get('start_date')
    end_date = house_dict.get('end_date')
    if not all([house_id, start_date, end_date]):
        return jsonify(status_code.ORDER_COMMIT_IS_NULL)
    start_time = datetime.strptime(start_date, '%Y-%m-%d')
    end_time = datetime.strptime(end_date, '%Y-%m-%d')
    if (end_time - start_time).days < 0:
        return jsonify(status_code.ORDER_COMMIT_TIME_ERROR)
    days = (end_time - start_time).days + 1
    house = House.query.get(house_id)
    total_price = house.price * days
    order = Order()
    order.days = days
    order.house_id = house_id
    order.user_id = user_id
    order.begin_date = start_time
    order.end_date = end_time
    order.house_price = house.price
    order.amount = total_price
    try:
        order.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@orders.route('/myorder/', methods=['GET'])
@is_login
def my_order():
    return render_template('orders.html')


@orders.route('/myorders/', methods=['GET'])
@is_login
def order_info():
    user_id = session['user_id']

    try:
        orders = Order.query.filter(Order.user_id == user_id)
        order_list = [order.to_dict() for order in orders]
        return jsonify(code=status_code.OK, order=order_list)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@orders.route('/lorders/', methods=['GET'])
# @is_login
def cus_orders():
    return render_template('lorders.html')


@orders.route('/cus_orders/', methods=['GET'])
@is_login
def all_cus_orders():
    user_id = session['user_id']
    try:
        house_list = House.query.filter(House.user_id == user_id)
        house_list_id = [house.id for house in house_list]
        order_list = Order.query.filter(Order.house_id.in_(house_list_id)).order_by(Order.id)
        lorder_list = [order.to_dict() for order in order_list]
        return jsonify(code=status_code.OK, lorders=lorder_list)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@orders.route('/lorder/<int:id>/', methods=['PATCH'])
# @is_login
def changestatus(id):
    status = request.form.get('status')
    order = Order.query.get(id)
    order.status = status
    if status == "REJECTED":
        content = request.form.get('rejected')
        order.comment = content
    try:
        order.add_update()
        return jsonify(status_code.SUCCESS)
    except:
        return jsonify(status_code.DATABASE_ERROR)
