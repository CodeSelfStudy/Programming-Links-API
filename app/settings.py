link_schema = {
    'title': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 255,
        'required':True,
    },
    'url': {
        'type': 'string',
        'minlength': 11, # e.g., http://t.co
        'maxlength': 2083, # IE limit,
        'required':True,
    },
    'description': {
        'type': 'string',

    },
    'tags': {
        'type': 'list',
        'items': [{'type': 'string'}],
    },
    'comments': {
        'type': 'list',
        'items': [{'type': 'string'}],
    }
}

links = {
    'schema': link_schema,
}

DOMAIN = {
    'links': links
}

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# TODO: get from env
MONGO_DBNAME = 'linksapi'

# Global resource and item methods
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
