from flask import jsonify
from sqlalchemy.orm import joinedload

from ..model.category import Category, CategorySchema
from ..model.entity import Session
from ..util.constant import NAME, CITY
from ..schema.item import ItemSchema
from ..model.item import Item


class ItemService():
        
    def list_items():
        with Session.begin() as session:
            query_items = session.query(Item).options(
                joinedload(CITY)).all()
            items = ItemSchema(many=True).dump(query_items)
            return jsonify(sorted(items, key=lambda i: i[NAME]))

    def getItem(id):
        with Session.begin() as session:
            query_item = session.query(Item).filter_by(id=id).one()
            print(ItemSchema().dump(query_item))
            return ItemSchema().dump(query_item)
    
    def deleteItem(id):
        with Session.begin() as session:
            item = session.query(Item).filter_by(id=id).one()
            session.delete(item)
            print(f"Item: {id} was deleted")
            return ItemService.list_items()

    # def create_item(request):
    #     with Session.begin() as session:
    #         posted_item = ItemSchema(
    #             load_only=(ITEM_SCHEMA_COLUMNS)).load(request)
    #         query_category = check_category(session, posted_item)
    #         query_state = check_state(session, posted_item)
    #         query_city = check_city(session, posted_item)
    #         state = StateSchema().dump(query_state)
    #         city = CitySchema().dump(query_city)
    #         category = CategorySchema().dump(query_category)

    #         item = Item(
    #             name=posted_item[NAME],
    #             artist=posted_item[ARTIST],
    #             purchased_price=posted_item[PURCHASED_PRICE],
    #             manufacturer=posted_item[MANUFACTURER],
    #             model_number=posted_item[MODEL_NUMBER],
    #             sku=posted_item[SKU],
    #             description=posted_item[DESCRIPTION],
    #             created_by="Loc Le",
    #             category_id=category['id'],
    #             state_id=state['id'],
    #             city_id=city['id']
    #         )
    #         session.add(item)
    #         print('New Item Added')
    #         return ItemSchema().dump(item)

    def list_categories():
        with Session.begin() as session:
            query_cat = session.query(Category).all()
            categories = CategorySchema(many=True).dump(query_cat)
        return jsonify(sorted(categories, key=lambda i: i[NAME]))
    
    def create_category(request):
        with Session.begin() as session:
            posted_category = CategorySchema(
                load_only=NAME).load(request)
            category = Category(name=posted_category[NAME])
            session.add(category)
            return CategorySchema().dump(category)
