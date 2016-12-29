# Sistema de Visualização de Dados Médicos

O código nesse repositório é referente a um sistema de visualização de dados médicos, proposto como desafio para demonstração de conhecimentos e técnicas em desenvolvimento web pela professora Carmen Maidantchik. 

## Estruturas utilizadas

Para o desenvolvimento desse projeto foi utilizando framework Flask com a versão do Python 3.5.2 . Mais detalhes sobre esse framework podem ser encontrados em:

- [Flask Guide](http://flask.pocoo.org/docs/0.12/)

Na parte de visualização foi utilizado o amplamente conhecido framework Bootstrap. Ademais, algumas estruturas CSS e Jquery públicas foram aproveitadas. Foram elas:

- [Panel table with filters (per column) with (checkbox)](http://bootsnipp.com/user/snippets/q8949)
- [Bootstrap 3D buttons](http://bootsnipp.com/snippets/featured/bootstrap-3d-buttons)
- [Advanced Dropdown Search](http://bootsnipp.com/snippets/featured/advanced-dropdown-search)
- [Multi Select Tiled Layout](http://bootsnipp.com/snippets/featured/multi-select-tiled-layout)



## Inicialização

Para executar o projeto basta extrair os arquivos desse repositório e depois, após ir no terminal até esse mesmo diretório, executar o comando:

```python
python app.apy
```

Feito isso o projeto será executado e está disponível em **[http://localhost:5000/](http://localhost:5000/)**

### Dependências

É necessário ter o Python 3 e o flask instalados. Para tal basta executar os seguintes comandos no terminal:

```
sudo apt-get update
sudo apt-get install python3
```

E em seguida

```
pip install flask
pip install ipython
```



## Funcionalidades básicas

As funcionalidades básicas do software são:

- Exibir todas as variáveis clínicas disponíveis sobre um determiando paciente;
- Exibir os dados de todos os pacientes em relação a uma determinada variável clínica;
- Permitir a seleção de variáveis clínicas customizadas e exibir informações de todos os paciente sobre elas, em conjunto;
- Permitir que usuários filtrem seus resultados de busca com base nas colunas exibidas.



## Utilização

Código sob a MIT License.