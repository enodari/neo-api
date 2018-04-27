from playhouse.shortcuts import model_to_dict
from models import Neo
import falcon


class NeoResource:
    def on_get(self, request, response, name=None):
        if name:
            try:
                data = model_to_dict(Neo.get(Neo.name ** name))  # Get by name (** = case-insensitive)
            except Neo.DoesNotExist:
                raise falcon.HTTPNotFound
        else:
            data = Neo.select(Neo.name, Neo.number).dicts()
        response.media = data


api = falcon.API()
api.add_route('/api/', NeoResource())
api.add_route('/api/{name}', NeoResource())
