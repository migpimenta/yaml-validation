from cerberus import Validator
import yaml


def load_doc():
    with open('./data/domain.yml', 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exception:
            raise exception


def validate_schema():
    schema = eval(open('./schema/schema.py', 'r').read())
    v = Validator(schema)
    doc = load_doc()
    print(v.validate(doc, schema))
    print(v.errors)


if __name__ == '__main__':
    validate_schema()
