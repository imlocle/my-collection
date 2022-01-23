from .constant import CATEGORY, CITY, STATE, NAME
from ..schema.location import StateSchema
from ..model.location import City, State
from ..model.category import Category, CategorySchema


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

def check_category(session, posted_item):
    try:
        query_cat = session.query(Category).filter_by(
            name=posted_item[CATEGORY][NAME]).one()
    except:
        category = Category(name=posted_item[CATEGORY][NAME])
        session.add(category)
        query_cat = session.query(Category).filter_by(
            name=posted_item[CATEGORY][NAME]).one()
    return query_cat
