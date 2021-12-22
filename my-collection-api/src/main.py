from flask import Flask, jsonify, request
from flask_cors import CORS

from .models.entity import Base, Session, engine
from .models.item import Item, ItemSchema
from .utils.constants import ITEM_SCHEMA_COLUMNS

app = Flask(__name__)
cors = CORS(app)

# generate database schema
Base.metadata.create_all(engine)


@app.route('/api')
def home():
    return "bye"


@app.route('/api/items')
def list_items():
    with Session.begin() as session:
        item_objects = session.query(Item).all()
        schema = ItemSchema(many=True)
        items = schema.dump(item_objects)
    return jsonify(sorted(items, key=lambda i: i['name']))


@app.route('/api/item', methods=["POST"])
def create_item():
    with Session.begin() as session:
        posted_item = ItemSchema(
            only=(ITEM_SCHEMA_COLUMNS)).load(request.get_json())
        item = Item(**posted_item, created_by="Loc Le")
        session.add(item)
        new_item = ItemSchema().dump(item)
    return jsonify(new_item), 201


@app.route('/api/item/<id>', methods=["DELETE"])
def delete_item(id):
    with Session.begin() as session:
        item = session.query(Item).filter_by(id=id).one()
        session.delete(item)
    return list_items()


if __name__ == "__main__":
    app.run(debug=True)
