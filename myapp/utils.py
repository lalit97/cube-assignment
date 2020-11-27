from django.contrib.auth.models import User


def get_normalized_data(data):
    # normalize userid and get user
    userid = data.pop('userid')
    user = User.objects.get(id=userid)
    data['user'] = user.id

    # normalize latitude, longitude
    latitude, longitude = data.pop('latlong').split(',')
    data['latitude'] = latitude
    data['longitude'] = longitude

    # populate value field
    properties = data.get('properties')
    value = properties.get('value', None)
    data['value'] = value

    return data


def create_log(message):
    with open("./logs.txt", "a", encoding = "utf-8") as f:
        f.write(message)
