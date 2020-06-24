import jsonschema
import json
import glob, os

schema = json.load(open("/schemas/schemas/core/person.json"))
data = json.load(open("/schemas/schemas/test/sample.json"))
store = {}

for file in glob.glob("/schemas/schemas/core/*.json"):
    additionalschema = json.load(open(file))
    store[additionalschema["$id"]] = additionalschema

resolver = jsonschema.RefResolver.from_schema(schema, store=store)
validator = jsonschema.Draft7Validator(schema, resolver=resolver)
validator.validate(data, schema)