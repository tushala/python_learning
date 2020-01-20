import numbers


class Field:
    pass


class CharField(Field):
    def __init__(self, db_colum, max_length=None):
        self._value = None
        self.db_colum = db_colum
        if max_length is not None:
            if not isinstance(max_length, numbers.Integral) or max_length < 0:
                raise TypeError
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError
        if len(value) > self.max_length:
            raise ValueError
        self._value = value


class IntField(Field):
    def __init__(self, db_colum, min_value=None, max_value=None):
        self._value = None
        self.db_colum = db_colum
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral) or min_value < 0:
                raise TypeError
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral) or max_value < 0:
                raise TypeError
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError

        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise TypeError
        if value > self.max_value or value < self.min_value:
            raise ValueError
        self.value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        # return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_colum = value.db_colum
            if db_colum is None:
                db_colum = key.lower()
            fields.append(db_colum)
            value = getattr(self, key)
            values.append(str(value))
        sql = f"insert {self._meta['db_table']}({','.join(fields)}) value({','.join(values)})"


class User(BaseModel):
    name = CharField(db_colum="name", max_length=10)
    age = IntField(db_colum="age", min_value=0, max_value=99)

    class Meta:
        db_table = "user"


if __name__ == '__main__':
    user = User()
    user.name = "tushala"
    user.age = 28
    user.save()



