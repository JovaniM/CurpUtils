## NOTA: Este codigo ya no funciona debida a la incorporacion de un catpcha en la pagina del curl, no puedo de momento dar mantenimiento al codigo. 
# CurpUtils
Clase en python para obtener información relevante sobre datos del CURP (México), tal como: nombre, apellido, fecha de nacimiento y lugar de nacimiento.

# En la actual versión se implemento lo siguiente:
Se obtiene el CURP a partir del nombre, apellido, fecha nacimiento, etc.
# Modo de uso:
```python
#Para  obtener los datos relevantes con la ayuda del CURP
curp_fetcher = CurpUtils()
data,message = curp_fetcher.getDataFromCurp("XXXX000000XXXXXX00") #CURP valido

#Para obtener el CURP con los datos relevantes
curp_fetcher = CurpUtils()
data, message = curp_fetcher.getCurpFromData({
                                    'claveEntidad': 'XX',
                                    'nombres': 'NOMBRE(S)',
                                    'primerApellido': 'APELLIDO P.',
                                    'segundoApellido': 'APELLIDO M.',
                                    'fechaNacimiento': 'dd/mm/yyyy',
                                    'sexo': 'M|F'})
```
# Restricciones
<p><b>claveEntidad <span style="color:blue;">[Requerido]</span></b> es una nomenclatura de dos letras que identifica a cada estado de la republica mexicana, entre los valores posibles estan los siguientes:</p>
<table>
  <thead>
    <th>claveEntidad</th>
    <th>Estado</th>
  </thead>
  
  <tbody>
    <tr>
      <td><b>AS</b></td>
      <td>Aguascalientes</td>
    </tr>
    <tr>
      <td><b>BC</b></td>
      <td>Baja California</td>
    </tr>
  <tr>
      <td><b>BS</b></td>
      <td>Baja California Sur</td>
    </tr>
    <tr>
      <td><b>CC</b></td>
      <td>Campeche</td>
    </tr>
    <tr>
      <td><b>CL</b></td>
      <td>Coahuila</td>
    </tr>
    <tr>
      <td><b>CM</b></td>
      <td>Colima</td>
    </tr>
    <tr>
      <td><b>CS</b></td>
      <td>Chiapas</td>
    </tr>
    <tr>
      <td><b>CH</b></td>
      <td>Chihuahua</td>
    </tr>
    <tr>
      <td><b>DF</b></td>
      <td>Ciudad de México</td>
    </tr>
    <tr>
      <td><b>DG</b></td>
      <td>Durango</td>
    </tr>
    <tr>
      <td><b>GT</b></td>
      <td>Guanajuato</td>
    </tr>
    <tr>
      <td><b>GR</b></td>
      <td>Guerrero</td>
    </tr>
    <tr>
      <td><b>HG</b></td>
      <td>Hidalgo</td>
    </tr>
    <tr>
      <td><b>JC</b></td>
      <td>Jalisco</td>
    </tr>
    <tr>
      <td><b>MC</b></td>
      <td>Estado de México</td>
    </tr>
    <tr>
      <td><b>MN</b></td>
      <td>Michoacán</td>
    </tr>
    <tr>
      <td><b>MS</b></td>
      <td>Morelos</td>
    </tr>
    <tr>
      <td><b>NT</b></td>
      <td>Nayarit</td>
    </tr>
    <tr>
      <td><b>NL</b></td>
      <td>Nuevo León</td>
    </tr>
    <tr>
      <td><b>OC</b></td>
      <td>Oaxaca</td>
    </tr>
    <tr>
      <td><b>PL</b></td>
      <td>Puebla</td>
    </tr>
    <tr>
      <td><b>QT</b></td>
      <td>Querétaro</td>
    </tr>
    <tr>
      <td><b>QR</b></td>
      <td>Quintana Roo</td>
    </tr>
    <tr>
      <td><b>SP</b></td>
      <td>San Luis Potosí</td>
    </tr>
    <tr>
      <td><b>SL</b></td>
      <td>Sinaloa</td>
    </tr>
    <tr>
      <td><b>SR</b></td>
      <td>Sonora</td>
    </tr>
    <tr>
      <td><b>TC</b></td>
      <td>Tabasco</td>
    </tr>
    <tr>
      <td><b>TS</b></td>
      <td>Tamaulipas</td>
    </tr>
    <tr>
      <td><b>TL</b></td>
      <td>Tlaxcala</td>
    </tr>
    <tr>
      <td><b>VZ</b></td>
      <td>Veracruz</td>
    </tr>
    <tr>
      <td><b>YN</b></td>
      <td>Yucatán</td>
    </tr>
    <tr>
      <td><b>ZS</b></td>
      <td>Zacateca</td>
    </tr>
    <tr>
      <td><b>NE</b></td>
      <td>Nacido en el extranjero</td>
    </tr>
  </tbody>
</table>

<p><b>nombres <span style="color:blue;">[Requerido]</span></b> Aquí va el o los nombres de la persona, por ejemplo: <i>"ROBERTO"</i>, <i>"JUAN JOSE"</i>.</p>
<p><b>primerApellido <span style="color:blue;">[Requerido]</span></b> Aquí va el apellido paterno de la persona, por ejemplo: <i>"LOPEZ"</i>, <i>"MARTINEZ"</i>.</p>
<p><b>segundoApellido <span style="color:yellow;">[Opcional]</span></b> Aquí va el apellido materno de la persona, por ejemplo: <i>"PEREZ"</i>, <i>"GARCIA"</i>.</p>
<p><b>fechaNacimiento <span style="color:blue;">[Requerido]</span></b> Aquí va la fecha de nacimiento de la persona con formato dd/mm/yyyy, ejemplo <i>"30/05/1980"</i>, <i>"01/01/2000"</i>.</p>
<p><b>sexo <span style="color:blue;">[Requerido]</span></b> Define si la persona es hombre o mujer y esta determinada por la nomenclatura de una letra, donde:</p>
<table>
  <thead>
    <th>Nomenclatura</th>
    <th>Significado</th>
  </thead>
  <tbody>
    <tr>
      <td>H</td>
      <td>HOMBRE</td>
    </tr>
    <tr>
      <td>M</td>
      <td>MUJER</td>
    </tr>
  </tbody>
</table>
