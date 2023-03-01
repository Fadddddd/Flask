import json


class Device:

    # un constructeur
    def __init__(self, id_device: int, nom: str, marque: str, genre: str):
        self._id_device = id_device
        self._nom = nom
        self._marque = marque
        self._genre = genre

    # accesseurs et mutateurs

    @property
    def id_device(self):
        return self._id_device

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom : str):
        self._nom = nom

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, marque: str):
        self._marque = marque

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    #retour de l'objet Python en JSON
    def to_json(self):
        return self.__str__()

    #conversion de l'objet Python en JSON
    def __str__(self): #on doit donc def str et on va retourner un dict
        return json.dumps(dict(self), ensure_ascii=False)

    #Permet de creer un dictionnaire de la classe actuelle ac cles et valeurs
    def __iter__(self):
        yield from {
            "id_device": self._id_device,
            "nom" : self._nom,
            "marque" : self._marque,
            "genre" : self._genre
        }.items()

    @staticmethod
    def from_json(json_device):
        device_id: int = int(json_device['id_device'])
        return Device(device_id, json_device['nom'], json_device['marque'], json_device['genre'])
