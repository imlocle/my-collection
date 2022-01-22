from ..model.entity import Session
from ..model.state import StateSchema, State
from ..util.constant import NAME
from flask import jsonify, Blueprint

location_api = Blueprint('location', __name__)
                              
@location_api.route('/states')
def list_states():
    with Session.begin() as session:
        state_objects = session.query(State).all()
        schema = StateSchema(many=True)
        states = schema.dump(state_objects)
    return jsonify(sorted(states, key=lambda i: i[NAME]))