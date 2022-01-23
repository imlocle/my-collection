from flask import Blueprint, request
from marshmallow import pprint

from ..model.category import CategorySchema
from ..model.entity import Session
from ..model.item import Item
from ..schema.item import ItemSchema
from ..schema.location import CitySchema, StateSchema
from ..service.item_service import ItemService
from ..util.constant import (ARTIST, DESCRIPTION, ITEM_SCHEMA_COLUMNS,
                             MANUFACTURER, MODEL_NUMBER, NAME, PURCHASED_PRICE,
                             SKU)
from ..util.helper import check_category, check_city, check_state

item_api = Blueprint('item', __name__)

@item_api.route('/items')
def list_items():
    return ItemService.list_items()


@item_api.route('/item', methods=["POST"])
def create_item():
    pprint(request.get_json())
    with Session.begin() as session:
        posted_item = ItemSchema(
            load_only=(ITEM_SCHEMA_COLUMNS)).load(request.get_json())
        query_category = check_category(session, posted_item)
        query_state = check_state(session, posted_item)
        query_city = check_city(session, posted_item)
        state = StateSchema().dump(query_state)
        city = CitySchema().dump(query_city)
        category = CategorySchema().dump(query_category)

        item = Item(
            name=posted_item[NAME],
            artist=posted_item[ARTIST],
            purchased_price=posted_item[PURCHASED_PRICE],
            manufacturer=posted_item[MANUFACTURER],
            model_number=posted_item[MODEL_NUMBER],
            sku=posted_item[SKU],
            description=posted_item[DESCRIPTION],
            created_by="Loc Le",
            category_id=category['id'],
            state_id=state['id'],
            city_id=city['id']
        )
        session.add(item)
        print('New Item Added')
        return ItemSchema().dump(item)


@item_api.route('/item/<id>', methods=["GET", "PUT", "DELETE"])
def item(id):
    if request.method == 'GET':
        return ItemService.getItem(id)
    if request.method == 'DELETE':
        return ItemService.deleteItem(id)

@item_api.route('/item/categories')
def list_categories():
    return ItemService.list_categories()

@item_api.route('/item/category', methods=['POST'])
def create_category():
    return ItemService.create_category(request.get_json())
        