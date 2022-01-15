from flask import Flask, jsonify, request
from flask_cors import CORS
from marshmallow import pprint
from sqlalchemy.orm import joinedload

from .models.city import CitySchema
from .models.entity import Base, Session, engine
from .models.item import Item, ItemSchema
from .models.state import StateSchema, State
from .utils.constants import (CITY, DESCRIPTION, ITEM_SCHEMA_COLUMNS, NAME,
                              PURCHASED_PRICE, SKU)
from .utils.helper import check_city, check_state

app = Flask(__name__)
cors = CORS(app)

# generate database schema
Base.metadata.create_all(engine)


@app.route('/api')
def home():
    return 200


@app.route('/api/items')
def list_items():
    with Session.begin() as session:
        query_items = session.query(Item).options(
            joinedload(CITY)).all()
        items = ItemSchema(many=True).dump(query_items)
    return jsonify(sorted(items, key=lambda i: i[NAME]))


@app.route('/api/item', methods=["POST"])
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
        new_item = ItemSchema().dump(item)
        print('New Item Added')
    return jsonify(new_item), 201


@app.route('/api/item/<id>', methods=["GET", "DELETE"])
def item(id):
    with Session.begin() as session:
        if request.method == 'GET':
            query_item = session.query(Item).filter_by(id=id).one()
            item = ItemSchema().dump(query_item)
            return jsonify(item), 201
        if request.method == 'DELETE':
            item = session.query(Item).filter_by(id=id).one()
            session.delete(item)
    return list_items()


@app.route('/api/states')
def list_states():
    with Session.begin() as session:
        state_objects = session.query(State).all()
        schema = StateSchema(many=True)
        states = schema.dump(state_objects)
    return jsonify(sorted(states, key=lambda i: i[NAME]))


if __name__ == "__main__":
    app.run(debug=True)
