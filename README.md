# Web Crawler 1.0.0

**Data da Criação:**
15/08/2021

**Desenvolvedor criador:**
Carlos Oliveira

**Objetivo do Script:**
Vai coletar dados sobre Cloud Instances, nos sites da Vultr e Digital Ocean, e salvar no formato json e csv.

## Sumário

1. **[Endpoints](#Endpoints)** 
2. **[Ações](#Ações)** 
3. **[Changelog](#Changelog)**
4. **[BugFixes](#BugFixes)**

## Endpoints
Realiza requisição ao site da Vultr
* https://www.vultr.com/products/cloud-compute/ (GET)

Realiza requisição ao site da Digital Ocean - Tabela Regular
* https://www.digitalocean.com/pricing/ (GET)

Realiza requisição ao site da Digital Ocean - Tabelas Premium da Intel e AMD
* https://www.digitalocean.com/c91f2d98-7829554511fa4c770105.js (GET)

## Ações
##### 1 Faz o scrapy das paginas: Vultr e Digital Ocean, pelos endpoints
##### 2 Faz tratamento de texto no retorno dos endpoints e constrói um dict
##### 3 Printa no terminal os dados extraídos de forma tabulada
##### 4 Salva os dados em um banco de dados local, com data e ID específico
##### 5 Salva os dados em um documento CSV
##### 6 Salva os dados em um documento JSON

## Changelog

## BugFixes
