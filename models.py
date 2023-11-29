from peewee import Model, AutoField, CharField, DateTimeField, UUIDField

class BaseModel(Model):
    id = AutoField()

    class Meta:
        legacy_table_names = False

class PageView(BaseModel):
    timestamp = DateTimeField(null=True)
    page = CharField(max_length=32)
    user_uuid = UUIDField()
    source = CharField(max_length=32)