from peewee import SqliteDatabase, Model, CharField, DecimalField

db = SqliteDatabase('neos.db')


class Neo(Model):
    name = CharField(primary_key=True, unique=True)
    number = CharField(unique=True, null=True)
    absolute_magnitude = DecimalField()
    slope_parameter = DecimalField()
    perihelion = DecimalField()
    aphelion = DecimalField()

    class Meta:
        database = db
