# Nomenclatura software

## Plugin

I plugin hanno per quanto possibile la seguente nomenclatura
* org.asup.sys.xx.yyyy.zzzz (open source)
* org.asup.sys.et.xxxx (librerie terze)
* org.smeup.sys.ft (Eclipse feature As.UP)

Dove : 
* xx = applicazione (max 2 chars)
* yyyy = modulo (possibilmente 4 chars, max 6 chars)
* zzzz = implementazione (possibilmente max 4 chars)
* oooo = oggetto (max 7 chars)

## Codice
* Le interfacce openSource hanno dove possibile il prefisso 'Q'
* Le implementazioni di interfacce hanno dove possibile il postfisso 'Impl'
* Il nome xxxxx_ è riservato al generatore di codice Eclipse EMF
* Il nome _xxxxxx è riservato alle classi interne As.UP con possibile conflitto
* Le variabili qXxxxxx sono riservate a classi e metodi esterni As.UP


## Tecnologie

### Riservate As.UP
* base
* impl
* ibmi
* rpj
* test

### Java
* jdbc
* nio

### Eclipse
* cdo
* ecf
* emf
* e4
* dtp
* flux
* jdt
* jetty
* p2

### Terze parti
* antlr
* asf
* asm
* db2
* cron
* fb
* gnu
* json
* jtds
* jtopen
* lpg
* mssql
* mysql
* osgi
