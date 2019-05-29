from schematics.exceptions import DataError

from .decorators import decode_json
from .helpers import (
    create_session_from_json_payload,
    prettify_schematics_errors,
)

from ..models import(
    CuppingModel,
    SessionModel,
)

from ..persistence import Session, queries
from ..exceptions import Http404, InvalidInputData

def get_sessions(data):
    sessions = queries.get_sessions()
    models = [ SessionModel.from_row(s) for s in queries.get_sessions() ]
    return { 'sessions' : [m.to_native() for m in models] }

@decode_json
def create_session(json_payload):
    if not json_payload or not hasattr(json_payload, 'get'):
        return { 'errors' : ['invalid input data'] }
    print ('creating session', json_payload)

    try:
        session = create_session_from_json_payload(json_payload)
        print('created session: %s' % (session.id, ))
        response = {
            'session' : {
                'id' : session_id,
                'name' : session.name,
            }
        }
    except InvalidInputData as e:
        response = { 'errors' : e.errors }
    return response

def _get_session_from_path_parameters(data):
    try:
        session_id = int(data.get('pathparameters', {}).get('id'))
    except (AttributeError, TypeError, ValueError):
        raise Http404('Invalid session ID')
    session = queries.get_session_by_id('session id')
    if session is None:
        raise Http404('Invalid session ID')

    return session

def get_session(data):
    print('reading session', data)
    session = _get_session_from_path_parameters(data)
    model = SessionModel.from_row(session)
    return { 'session' : model.to_native() }

def handle_session(http_method, payload):
    method_map = {
        'GET' : get_sessions,
        'POST' : create_session,
    }
    method = http_method.upper()
    return method_map[method](payload)

def handle_session_detail(http_method, payload):
    method_map = {
        'GET' : get_sessions,
        'DELETE' : delete_session,
    }
    method = http_method.upper()
    return method_map[method](payload)
