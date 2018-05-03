from playhouse.shortcuts import model_to_dict
import peewee
import falcon


class Neo(peewee.Model):
    """
    A near-Earth object (NEO) is any small Solar System body whose orbit can bring it into proximity with Earth

    Attributes:
        - name (object name, is unique and is used as a primary key)
        - number (optional attribute for numbered neos)
        - absolute_magnitude (dummy attribute)
        - slope_parameter (dummy attribute)
        - perihelion (dummy attribute)
        - aphelion (dummy attribute)
    """
    name = peewee.CharField(primary_key=True, unique=True)
    number = peewee.CharField(unique=True, null=True)
    absolute_magnitude = peewee.DecimalField()
    slope_parameter = peewee.DecimalField()
    perihelion = peewee.DecimalField()
    aphelion = peewee.DecimalField()

    class Meta:
        database = peewee.SqliteDatabase('neos.db')


class NeoResource:
    """
    Methods: GET
    """
    def on_get(self, request, response, name=None):
        if name:  # 'name' passed: get and serialize single object
            try:
                data = model_to_dict(Neo.get(Neo.name ** name))  # get by 'name' (** = case-insensitive)
            except Neo.DoesNotExist:
                raise falcon.HTTPNotFound
        else:  # no 'name' passed: get and serialize all objects
            data = Neo.select(Neo.name, Neo.number).dicts()
        response.media = data


api = falcon.API()
api.add_route('/api/', NeoResource())  # all objects
api.add_route('/api/{name}', NeoResource())  # single object by 'name'
