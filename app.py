import json

from flask import Flask, request

from models.Device import Device

app = Flask(__name__)

list_device: list = []


# renvoie une donnee
@app.route('/', methods=['GET'])
def get_all_devices():  # put application's code here
    return json.dumps(
        list_device)  # loads : takes in a string and returns a json object dumps : takes in a json object and returns a string


# va creer une donnee
@app.route('/', methods=['POST'])
def create_object():  # put application's code here
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = json.loads(request.data)
        list_device.append(data)
        print(request.headers.get('Content-Type'))
        return True
    return False


# modifie un objet
@app.route('/', methods=['PUT'])
def modify_object():  # put application's code here
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data: Device = json.loads(request.data)
        list_device.append(data)
        delete_object(data.id)
        list_device.append(data)


# supprime un objet
@app.route('/<id>', methods=['DELETE'])
def delete_object(id: int):  # put application's code here
    for device in list_device:
        if device._id == id:
            list_device.remove(device)


if __name__ == '__main__':
    app.run()
