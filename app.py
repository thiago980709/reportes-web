from flask import Flask, jsonify,request,render_template,send_file
import requests
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import config




app = Flask(__name__,template_folder='templates')

app.config['UPLOAD_FOLDER'] = './reportes'

encargado = ['Andres Arango','Camilo Sanmartin','Santiago Castaneda','Juan Bernardo','Pepito perez']


@app.route('/listarReportes',methods=['GET'])
def listarReporte():
    reportes = requests.get('https://reportes-api-2q2b2mja4a-ue.a.run.app/reporte').json()
    return render_template('listarReporte.html',reportes=reportes)

@app.route('/crearReportes',methods=['GET'])
def crearReporte():
    return render_template('crearReporte.html',encargado=encargado)



@app.route("/guardarReporte",methods=['POST'])
def guardarReporte():
    reporte = dict(request.values)
    archivo = request.files['archivoDir']
    nombre = secure_filename(archivo.filename)
    ##archivo.save(os.path.join(app.config['UPLOAD_FOLDER'],nombre))
    rutaReporte = '../reportes/'+nombre
    reporte['archivoDir'] = rutaReporte
    reporte['estado'] = 'Pendiente'
    reporte['resultadoDir'] = nombre
    requests.post('https://reportes-api-2q2b2mja4a-ue.a.run.app/reporte',json=reporte)
    return(listarReporte())


app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)