# Importing XML library and doing basic parsing of the file
from xml.dom import minidom
xmldoc = minidom.parse("pacientes.xml")
doc = xmldoc.getElementsByTagName("doc")[0]

# patientInfo will be an array of dictionarys. Every entry os this array will be a dict
# with information about one specific patient
patientInfo = {}
numberOfPatients = doc.getElementsByTagName("paciente").length
numberOfPatientInfos = {}

binaryAnswerPositive = ["sim","verdadeiro"]
binaryAnswerNegative = ["nao","negativo","falso"]
attributes = []
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

data = patientInfo[1]["logradouro"].firstChild
print(data)