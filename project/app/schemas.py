from marshmallow import fields

from project.lib import ExcludeSchema

__all__ = ("SurnameSchema", )


class SurnameSchema(ExcludeSchema):
    surname = fields.Str(required=True, allow_none=False)
