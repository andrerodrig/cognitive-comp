# DSM - Disasters on Social Media

Este projeto tem como objetivo estudar a aplicação de técnicas de NLP para predição de alertas relevantes de desastres ocorridos. O dataset em uso é o _Disasters on Social Media_, que possui mais de 10 mil tweets selecionados a partir de buscas feitas no tweeter.

### Pré-requisitos:

- [Python 3.7+](https://www.python.org/downloads/)
- pip
- [Poetry](https://python-poetry.org/)

### Instalação:

- Clonar o projeto
- Dentro da pasta do projeto executar:

```
$ poetry install
```

### Comandos

- Para conseguir rodar os comandos do `invoke` é preciso estar dentro da virtualenv gerada pelo poetry, para isso, execute:

```
$ poetry shell
```

Após isso, é possivel baixar o dataset utilizado.

```
$ inv get-data
```