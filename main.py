import json


def is_json(func):

    def wrapper(file_name: str):
        if file_name.endswith('.json'):
            result = func(file_name)
        else:
            result = 'not json file.'

        return result

    return wrapper


@is_json
def to_dict(file_name: str):
    with open(file=file_name) as f:
        data = json.load(f)

    return data


r = to_dict('db.json')
print(r)
