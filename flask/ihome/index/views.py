from flask import Blueprint, render_template, jsonify, session, request
from sqlalchemy import or_

from APP.models import Area, House, User, Order
from utils import status_code

indexs = Blueprint('index', __name__)


@indexs.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@indexs.route('/getarea/')
def getarea():
    try:
        username = ''
        if 'user_id' in session:
            user_id = session['user_id']
            user = User.query.get(user_id)
            username = user.to_basic_dict()
        area_list = Area.query.all()
        house = House.query.order_by(House.id.desc()).limit(3).all()
        areas = [area.to_dict() for area in area_list]
        houses = [house_one.to_dict() for house_one in house]
        return jsonify(code=status_code.OK, users=username, area=areas, house=houses)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@indexs.route('/search/', methods=['GET'])
def search():
    return render_template('search.html')


@indexs.route('/allsearch/', methods=['GET'])
def allsearch():
    search_dict = request.args
    area_id = search_dict.get('aid')
    start_date = search_dict.get('sd')
    end_date = search_dict.get('ed')
    sk = search_dict.get('sk')

    if sk == 'price-inc':
        sort_key = 'price'
    elif sk == 'price-des':
        sort_key = '-price'
    elif sk == 'booking':
        sort_key = 'order_count'
    else:
        sort_key = '-id'

    try:
        if area_id == '':
            houses = House.query.order_by(sort_key).all()
        else:
            houses = House.query.order_by(sort_key).filter(House.area_id == area_id)

        if start_date == '':
            can_not_orders = Order.query.all()
        else:
            if end_date == '':
                can_not_orders = Order.query.filter(Order.end_date >= end_date)
            else:
                can_orders = Order.query.filter(or_(Order.begin_date > end_date,
                                                    Order.end_date < start_date))
                can_order_list = [order.id for order in can_orders]

                can_not_orders = Order.query.filter(Order.id not in can_order_list)

        can_not_list = [order.house_id for order in can_not_orders]

        show_house = []

        for house in houses:
            if house.id not in can_not_list:
                show_house.append(house.to_dict())

        areas = Area.query.all()
        alist = [area.to_dict() for area in areas]

        return jsonify(code=status_code.OK, alist=alist, showhouse=show_house)
    except:
        return jsonify(status_code.DATABASE_ERROR)
