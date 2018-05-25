import re

import os
from flask import Blueprint, render_template, session, jsonify, request

from APP.settings import upload_dir
from utils import status_code
from APP.functions import is_login
from APP.models import User, House, Area, Facility, ihome_house_facility, HouseImages

myhouse = Blueprint('myhouse', __name__)


@myhouse.route('/myhouse/', methods=['GET'])
@is_login
def my_house():
    return render_template('myhouse.html')


@myhouse.route('/auth_house/', methods=['GET'])
@is_login
def show_house():
    user_id = session['user_id']
    house_list = []
    try:
        houses = House.query.filter(House.user_id == user_id)
        for house in houses:
            housedict = house.to_dict()
            house_list.append(housedict)
        return jsonify(code=status_code.OK, house_list=house_list)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@myhouse.route('/auth/', methods=['GET'])
@is_login
def my_house_auth():
    user_id = session['user_id']
    try:
        user = User.query.get(user_id)
        if user.id_card != None and user.id_name != None:
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.HOUSE_USER_AUTH_IS_NULL)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@myhouse.route('/newhouse/', methods=['GET'])
@is_login
def my_new_house():
    return render_template('newhouse.html')


@myhouse.route('/get_info/', methods=['GET'])
@is_login
def get_area():
    try:
        areas = Area.query.all()
        facilities = Facility.query.all()
        areas_list = []
        facility_list = []
        for area in areas:
            areas_list.append(area.to_dict())
        for facility in facilities:
            facility_list.append(facility.to_dict())
        return jsonify(code=status_code.OK, areas_list=areas_list, facility_list=facility_list)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@myhouse.route('/newhouse/', methods=['POST'])
@is_login
def mynewhouse():
    user_id = session['user_id']
    house_dict = dict(request.form)
    title = house_dict['title']
    price = house_dict['price']
    area_id = house_dict['area_id']
    address = house_dict['address']
    room_count = house_dict['room_count']
    acreage = house_dict['acreage']
    unit = house_dict['unit']
    capacity = house_dict['capacity']
    beds = house_dict['beds']
    deposit = house_dict['deposit']
    min_days = house_dict['min_days']
    max_days = house_dict['max_days']
    facilites = house_dict['facility']
    if not all([title, price, area_id, address, room_count,
                acreage, unit, capacity, beds, deposit,
                min_days, max_days, facilites]):
        return jsonify(status_code.HOUSE_UPLOAD_INFO_ERROR)
    house = House()
    house.user_id = user_id
    house.title = title
    house.price = price
    house.area_id = area_id
    house.address = address
    house.room_count = room_count
    house.acreage = acreage
    house.unit = unit
    house.capacity = capacity
    house.beds = beds
    house.deposit = deposit
    house.min_days = min_days
    house.max_days = max_days
    for facility in facilites:
        fac = Facility.query.get(facility)
        house.facilities.append(fac)
    try:
        user = User.query.get(user_id)
        house.add_update()
        return jsonify(code=status_code.OK, houseid=house.id)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@myhouse.route('/newhouse/', methods=['PUT'])
@is_login
def myhouseimg():
    file = request.files
    house_id = request.form.get('house_id')
    if 'house_image' in file:
        image_file = file['house_image']
        if not re.match('^image/.*$', image_file.mimetype):
            return jsonify(status_code.HOUSE_UPLOAD_IMG_TYPE_ERROR)
        img_name = image_file.filename
        url = os.path.join(upload_dir, img_name)
        # 保存图片
        image_file.save(url)

        house = House.query.get(house_id)
        img_url = os.path.join('/static/uploads/', img_name)
        try:
            houseimg = HouseImages()
            houseimg.house_id = house_id
            houseimg.url = img_url
            houseimg.add_update()
            house.images.append(houseimg)
            if house.index_img_url == '':
                house.index_img_url = img_url
            house.add_update()
            return jsonify(code=status_code.OK, imgurl=img_url)
        except:
            return jsonify(status_code.DATABASE_ERROR)
    else:
        return jsonify(status_code.HOUSE_UPLOAD_IMG_ERROR)


@myhouse.route('/detail/', methods=['GET'])
@is_login
def mydetail():
    return render_template('detail.html')


@myhouse.route('/details/', methods=['GET'])
@is_login
def details():
    user_id = session['user_id']
    house_id = request.args.get('id')
    try:
        house = House.query.get(house_id)
        is_self = 0
        if user_id == house.user_id:
            is_self = 1
        return jsonify(code=status_code.OK, house=house.to_full_dict(), is_self=is_self)
    except:
        return jsonify(status_code.DATABASE_ERROR)


@myhouse.route('/book/', methods=['GET'])
@is_login
def my_book():
    return render_template('booking.html')


@myhouse.route('/books/<int:id>/', methods=['GET'])
@is_login
def bookapi(id):
    house_id = id
    try:
        house = House.query.get(house_id)
        return jsonify(code=status_code.OK, house=house.to_dict())
    except:
        return jsonify(status_code.DATABASE_ERROR)
