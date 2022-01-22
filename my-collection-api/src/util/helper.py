from marshmallow.utils import pprint
from .constant import CITY, STATE, NAME
from ..model.state import State, StateSchema
from ..model.city import City


def check_state(session, posted_item):
    try:
        query_state = session.query(State).filter_by(
            name=posted_item[STATE][NAME]).one()
    except:
        state = State(name=posted_item[STATE][NAME],
                      abrv=posted_item[STATE]['abrv'])
        session.add(state)
        query_state = session.query(State).filter_by(
            name=posted_item[STATE][NAME]).one()
    return query_state


def check_city(session, posted_item):
    try:
        query_city = session.query(City).filter_by(
            name=posted_item[CITY][NAME]).one()
    except:
        query_state = session.query(State).filter_by(
            name=posted_item[STATE][NAME]).one()
        state = StateSchema().dump(query_state)
        city = City(name=posted_item[CITY][NAME], state_id=state['id'])
        session.add(city)
        query_city = session.query(City).filter_by(
            name=posted_item[CITY][NAME]).one()
    return query_city
