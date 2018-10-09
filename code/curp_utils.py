###################################################################
# Author: Jovani Martín Martínez González
# Contact:
# Mobile: +52 2281187906
# E-mail: jovanimmg@gmail.com
##################################################################

import json
import re
import requests

class CurpUtils:
    url = None
    headers = None
    required_data = None
    validate_data = None

    def __init__(self):
        self.url = "https://www.gob.mx/v1/renapoCURP/consulta"
        self.headers = {
            'host': 'www.gob.mx',
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'referer': 'https://www.gob.mx/',
            'content-type': 'application/json',
            'keep-alive': 'timeout = 5, max = 100'
        }

        self.required_data = [
            'claveEntidad',
            'fechaNacimiento',
            'nombres',
            'primerApellido',
            'sexo']

        self.validate_data = {
            'claveEntidad': self.validate_clave,
            'fechaNacimiento': self.validate_date,
            'nombres': self.validate_names,
            'primerApellido': self.validate_names,
            'sexo': self.validate_sex
        }

    def getDataFromCurp(self, curp):
        payload = json.dumps({
            "curp": curp,
            "tipoBusqueda": "curp"
        })

        r = requests.post(self.url, data=payload, headers=self.headers)
        if r.status_code == 200:
            json_response = json.loads(r.text)

            if json_response['codigo'] != "01":
                return None, json_response['mensaje']

            return json_response['registros'][0], json_response['mensaje']
        return None, r.text

    def getCurpFromData(self, data):
        for value in self.required_data:
            if not value in data:
                return None, value + " is required!"
            if not self.validate_data[value](data[value]):
                return None, "El campo " + value + " con el valor " + data[value] + " no tiene el formato correcto."

        #segundoApellido is not required so we need to validate out the loop
        if not 'segundoApellido' in data and not self.validate_names(data['segundoApellido']):
            return None, "El campo segundoApellido no tiene el formato correcto."

        data.update({"tipoBusqueda": "datos"})

        payload = json.dumps(data)

        r = requests.post(self.url, data=payload, headers=self.headers)
        if r.status_code == 200:
            json_response = json.loads(r.text)

            if json_response['codigo'] != "01":
                return None, json_response['mensaje']

            return json_response['registros'][0], json_response['mensaje']
        return None, r.text

    def validate_clave(self, clave):
        return clave.upper() in ['AS', 'BC', 'BS', 'CC', 'CL', 'CM', 'CS', 'CH', 'DF', 'DG', 'GT', 'GR',
                                   'HG', 'JC', 'MC', 'MN', 'MS', 'NT', 'NL', 'OC', 'PL', 'QT', 'QR', 'SP',
                                   'SL', 'SR', 'TC', 'TS', 'TL', 'VZ', 'YN', 'ZS', 'NE']

    def validate_date(self, date):
        pattern = re.compile("^(3[0-1]|[1-2][0-9]|0[1-9])/(0[1-9]|1[0-2])/[1-2][0-9]{3}$")
        return pattern.match(date)

    def validate_names(self, name):
        return len(name.replace(" ","")) > 0

    def validate_sex(self, sex):
        return sex.upper() in ['M', 'H']

