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


p_similarity = []
att_similarity = []
temp = []
temp2 = []
for k in range(0,len(patientInfo)):
    temp.append([])
    temp2.append([])
for k in range(0,len(patientInfo)):
    p_similarity.append(temp[:])
    att_similarity.append(temp2[:])

for att in attributes:
    for i in range(0,len(patientInfo)):
        for j in range(0,len(patientInfo)):
            if(att in patientInfo[i] and att in patientInfo[j]):
                if (patientInfo[i][att].firstChild != None and patientInfo[j][att].firstChild != None):
                    if (patientInfo[i][att].firstChild.data == patientInfo[j][att].firstChild.data):    
                        p_similarity[i][j].append(att)
                        att_similarity[i][j].append(patientInfo[i][att].firstChild.data)








# Removing duplicate names from the array

attributes = list(set(attributes))
attributes.sort()
friendlyPatientInfo = []
friendlyAttributes = attributes[:]
## First Element of the list is always the frindly name of that list

## Hardcode clusters

h_drinks = [["Bebidas","Informações sobre o consumo de bebidas alcolicas"],
"Cachaca","Cerveja","Vinho","Whisky","bebidaPreferida","outraBebidaPreferida","tomaBebida"]

h_habits = [["Hábitos","Informações sobre hábitos do paciente"],
"anosFuma","bebeManha","cigarrosDia","habitoFumar"]

h_devices = [["Dispositivos domésticos","Informações sobre utensílios que o paciente utiliza/possui em sua casa ou utiliza no dia a dia"],
"aspiradorPo","automovel","dvd","freezer","geladeiraDuplex","geladeiraSimples","maquinaLavar","radio","tv"]

h_personalInfo = [["Informações Pessoais"," "],
"profissionalSaude","municipioEndereco","moradorRua","morouOutro","rendaFamiliarPassado","telefone1","telefone2","usuarioDrogas","tempoEnderecoAtual","sexo","rendaFamiliarAtual","ocupacao","outraFuncao","quantosAnos","morouTuberculose","moradorAsilo","atividadeTrabalho","bairroEndereco","cidadeNaturalidade","estadoCivil","estadoEndereco","estadoNaturalidade","estudaMomento","exDetento","grauInstrucao","grauInstrucaoChefe",]

h_homeInfo = [["Informações de residência","Informações a residência do paciente"],
"numero","numeroComodos","numeroDormitorios","numeroPessoas","cep","banheiro","cep","complemento","logradouro","latitude","longitude",]

h_symptoms = [["Sintomas","Sintomas que foram analisados no paciente"],
"cansaco","dor","emagrecimento","escarro","faltaAr","febre","rouquidao","senteCulpa","sinaisSintomas","tosse","ulcera"]

h_exams = [["Exames","Informaçoes sobre exames ao qual o paciente foi submetido"],
"adaLiquidoPleural","alteracoesExameFisico","antigenos","areaAcometida","assintomatico","associacaoAlteracoesPulmonares","baarEscarro1","baarEscarro2","baarLp","cancer","cargaTabagica","comorbidades","cultura","culturaMicrobacterias",
"derramePleuralLivre","diabetes","diagnosticoTB","doencaHepaticaCronica","dpoc","exame","exameFisico","exameHistopatologico","expectoracao","hemoptise","hiporexia",
"inalaFumaca","infeccaoHiv","insuficienciaRenalCronica","intensidade1","intensidade2","intensidadeInduzido","internadoUltimosAnos","leitor","linfadenomegalia","medio",
"medioDireito","medioEsquerdo","metodo","metodoCultura","milimetrosEnduracao","observacoes","observacoesUltima","outrasAlteracoes","outroExame",
"outroTratamento","outrosSintomas","probabilidadeAposExames","probabilidadeComAvaliacao","probabilidadeSemAvaliacao","provaTuberculinicaReatora","quaisComorbidadesOutras","qualAlteracao","qualAssociacao","riscoTbMdr",
"sarcoidose","silicose","sorologiaLp","sudorese","superior","superiorDireito","superiorEsquerdo","tecnicaUtilizada","telerradiografia","volumeDerramePleural"]

## Clustering similar attributes
results = [["Resultados de exames","Resultados dos exames realizados pelo paciente"]]
select = [["Variáveis de seleção","Variáveis nas quais o paciente ou examinador marcou verdadeiro ou falso para determinada informação"]]
tuberculosis = [["Informações sobre tuberculose","Informações relacionadas a tuberculose"]]
txt = [["Variaveis TXT","Variáveis com o prefixo TXT"]]
used =[]
others = [["Outras variaveis"," "]]



# Select variables group
for i in attributes:
    if("selecionou" in i.lower()):
        select.append(i)
        attributes = attributes[:attributes.index(i)] + attributes[attributes.index(i)+1:]
# Results group
for i in attributes:
    if("resultado" in i.lower() and i.lower() != "resultado" ):
        results.append(i)
        attributes = attributes[:attributes.index(i)] + attributes[attributes.index(i)+1:]

# Tuberculosis group
for i in attributes:
    if("tuberculose" in i.lower()):
        tuberculosis.append(i)

# TXT group
for i in attributes:
    if("txt_" in i.lower()):
        txt.append(i)
        attributes = attributes[:attributes.index(i)] + attributes[attributes.index(i)+1:]
##

#Creating a list of lists with grouped data
Groupdata = []
Groupdata.append(h_drinks)
Groupdata.append(h_habits)
Groupdata.append(h_devices)
Groupdata.append(h_personalInfo)
Groupdata.append(h_homeInfo)
Groupdata.append(h_symptoms)
Groupdata.append(results)
Groupdata.append(select)
Groupdata.append(tuberculosis)
Groupdata.append(h_exams)
Groupdata.append(txt)
for i in attributes:
    used = False
    for group in Groupdata:
        if(i in group):
            used = True
    if(used == False):
        others.append(i)

Groupdata.append(others)



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
    return render_template("atributos.html",attributes = friendlyAttributes,Groupdata = Groupdata)

@app.route("/paciente/<int:patient_id>")
def html_page(patient_id):
    return render_template("resultado-paciente.html",patientInfo = patientInfo, patient_id = patient_id, attributes = attributes )

@app.route("/filtro/<dado>")
def resultado_filtro(dado):
    return render_template("resultado_filtro.html",patientInfo = patientInfo,numberOfPatients= numberOfPatients,dado=dado)


@app.route('/resultado')
def resultado():
    return render_template("resultado-filtro-multiplo.html",patientInfo = patientInfo,numberOfPatients= numberOfPatients)


@app.route('/similaridade/')
def similarity():
    return render_template("similaridade.html",att_similarity = att_similarity,p_similarity = p_similarity ,c=2)

app.run()