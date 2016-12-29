# Importing XML library and doing basic parsing of the file
from xml.dom import minidom
xmldoc = minidom.parse("pacientes.xml")
doc = xmldoc.getElementsByTagName("doc")[0]

# patientInfo will be an array of dictionarys. Every entry os this array will be a dict
# with information about one specific patient
patientInfo = {}
numberOfPatients = doc.getElementsByTagName("paciente").length
numberOfPatientInfos = {}

# Attributes will be a list with all attributes names inside the dataset
attributes = []

# This snippet fill in the patientInfo and create the specific dicts for every patient
for i in range(numberOfPatients):
    temp_info = {}
    paciente = doc.getElementsByTagName("paciente")[i]
    attributeNumber =  doc.getElementsByTagName("paciente")[i].childNodes.length
    numberOfPatientInfos[i]= attributeNumber
    for j in range(1,attributeNumber,2):
        attributeName = paciente.childNodes[j].tagName
        temp_info[attributeName] = paciente.getElementsByTagName(attributeName)[0]
        attributes.append(attributeName)
    patientInfo[i] = temp_info

# Removing duplicate names from the array

attributes = list(set(attributes))
attributes.sort()



from flask import Flask
from flask import render_template
import os
from json import dumps

app = Flask("cern")
@app.route("/")
def load_index():
    return render_template("index.html", attributes = attributes,c = 0,numberOfPatients =numberOfPatients)

@app.route("/atributos")
def selecionar_atributos():
    return render_template("atributos.html",attributes = attributes)

@app.route("/paciente/<int:patient_id>")
def html_page(patient_id):
    return render_template("resultado-paciente.html",patientInfo = patientInfo, patient_id = patient_id, attributes = attributes )

@app.route("/filtro/<dado>")
def resultado_filtro(dado):
    return render_template("resultado_filtro.html",patientInfo = patientInfo,numberOfPatients= numberOfPatients,dado=dado)


@app.route('/resultado')
def resultado():
    return render_template("resultado-filtro-multiplo.html",patientInfo = patientInfo,numberOfPatients= numberOfPatients)

app.run()