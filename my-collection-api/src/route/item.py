from flask import Blueprint, jsonify, request
from marshmallow import pprint
from sqlalchemy.orm import joinedload

from ..model.city import CitySchema
from ..model.entity import Session
from ..model.item import Item, ItemSchema
from ..model.state import StateSchema
from ..util.constant import (CITY, DESCRIPTION, ITEM_SCHEMA_COLUMNS, NAME,
                             PURCHASED_PRICE, SKU)
from ..util.helper import check_city, check_state

item_api = Blueprint('item', __name__)

@item_api.route('/items')
def list_items():
    with Session.begin() as session:
        query_items = session.query(Item).options(
            joinedload(CITY)).all()
        items = ItemSchema(many=True).dump(query_items)
    return jsonify(sorted(items, key=lambda i: i[NAME]))


@item_api.route('/item', methods=["POST"])
def create_item():
    with Session.begin() as session:
        posted_item = ItemSchema(
            load_only=(ITEM_SCHEMA_COLUMNS)).load(request.get_json())
        pprint(posted_item)
        query_state = check_state(session, posted_item)
        query_city = check_city(session, posted_item)
        state = StateSchema().dump(query_state)
        city = CitySchema().dump(query_city)

        item = Item(
            name=posted_item[NAME],
            purchased_price=posted_item[PURCHASED_PRICE],
            sku=posted_item[SKU],
            description=posted_item[DESCRIPTION],
            created_by="Loc Le",
            state_id=state['id'],
            city_id=city['id']
        )
        session.add(item)
        print('New Item Added')
        return ItemSchema().dump(item)


@item_api.route('/item/<id>', methods=["GET", "PUT", "DELETE"])
def item(id):
    with Session.begin() as session:
        if request.method == 'GET':
            query_item = session.query(Item).filter_by(id=id).one()
            return ItemSchema().dump(query_item)
        if request.method == 'DELETE':
            item = session.query(Item).filter_by(id=id).one()
            session.delete(item)
            return list_items()
