from flask import Flask, jsonify, request
from flask_cors import CORS
from .entities.entity import Session, engine, Base
from .entities.item import Item, ItemSchema

app = Flask(__name__)
cors = CORS(app)

# generate database schema
Base.metadata.create_all(engine)


@app.route('/')
def home():
    return "bye"


@app.route('/items')
def list_items():
    session = Session()
    item_objects = session.query(Item).all()

    schema = ItemSchema(many=True)
    items = schema.dump(item_objects)

    session.close()
    return jsonify(items)


@app.route('/item', methods=["POST"])
def create_item():
    print(request.data)
    posted_item = ItemSchema(
        only=('name', 'purchased_price', 'description')).load(request.get_json())
    item = Item(**posted_item, location='', sku='', created_by="Loc Le")
    session = Session()
    session.add(item)
    session.commit()

    new_item = ItemSchema().dump(item)
    session.close()
    return jsonify(new_item), 201


@app.route('/item/<id>', methods=["DELETE"])
def delete_item(id):
    session = Session()
    obj = session.query(Item).filter_by(id=id).one()
    session.delete(obj)
    session.commit()
    session.close()
    return list_items()


if __name__ == "__main__":
    app.run(debug=True)
