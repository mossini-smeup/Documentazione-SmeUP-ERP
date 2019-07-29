## Obiettivo
Rappresentare una serie di oggetti su si una mappa.
Le rappresentazioni possibili sono : 
* URL , vengono rappresentati gli oggetti su di una mappa statica. La mappa si autoregola in funzione degli oggetti presenti
* PERCORSO , vengono rappresentati gli oggetti su di una mappa dinamica e gli stessi legati fra loro in ordine cronologico.
* BROWSER , la mappa viene costruita in locale. Questa tecnica permette una personalizzazione della mappa.

## Limitazioni
* Sono gestiti al massimo 100 oggetti.
* La rappresentazione si basa su Google.

## Struttura Script
L'installatore deve definire la propria struttura di rappresentazione nello script che deve risiedere nel sorgente**SCP_SET**.
Il nome dello script deve essere composto da una parte fissa (LOA29_) e una parte variabile che indica il gruppo sotto cui riunire una serie di rappresentazioni.
All'interno dello script devono essere specificati almeno una sezione, una sottosezione e un paragrafo per la rappresentazione.
(Lo script è composto da due parti, la prima carattere e la seconda numerica, permettendo così la generazione di script meno corposi e semplici da mantenere.
La parte carattere non deve eccedere gli 8 caratteri, mentre la parte numerica deve essere lunga 2.)

 ### Tag dello script
 Elenco delle tag e del loro significato

**SEZ**Sezione

| Attributo|Significato|Descrizione |
| ---|----|----|
| Cod|Codice|Ragguppa per omogeneità i modelli di testo |
| Txt|Descrizione|Significato del gruppo |
| 


**SUB**Sotto sezione

| Attributo|Significato|Descrizione |
| ---|----|----|
| Cod|Codice|Identifica in maniera univoca il modello di testo |
| Txt|Descrizione|Significato del modello |
| 


**A29.IN**Oggetti in ingresso
Permette di impostare il modello di recupero degli oggetti.

| Attributo|Significato|Valore|Descrizione |
| ---|----|----|----|
| Txt|Descrizione|Significato del modello |
| Tip|Tipo modello|SQL|Comando sql |
| ||LIS|Lista di oggetti dal carrello |
| ||FUN|Servizio |
| Par|Parametro modello SQL||Comando SQL da eseguire |
| |Parametro modello LIS||IT(Tipo Carrello) IK(Oggetto carrello) IC(Codice carrello) |
| |Parametro modello FUN||Funzione da eseguire |
| 


**A29.SET**Definizione oggetto sulla mappa
Permette di impostare gli attributi dell'oggetto sulla mappa.

| Attributo|Significato|Descrizione |
| ---|----|----|
| Txt|Descrizione|Significato del modello |
| Ogge|Oggetto|Determina la colonna da cui prelevare l'oggetto |
| Codi|Codice|Determina la colonna da cui prelevare il codice |
| Mark|Marker|Determina la colonna da cui prelevare l'indirizzo su cui posizionare l'oggetto. |
| ||Se l'oggetto è una provincia e il marcatore non è definito, si assume, Codice provincia e descrizione della nazione |
| ||Se l'oggetto è un contatto e il marcatore non è definito, si assume,  Località, provincia, cap , indirizzo e nazione |
| Label|Label|Nome da visualizzare sulla mappa |
| ||Se in modalità URL, viene generato un progressivo di 1 carattere |
| ||In tutti gli altri casi viene esposta la descrizione dell'oggetto |
| Size|Dimensioni|Dimensione in pixel della mappa in formato (111x222) |
| IOg|Icona browser da oggetto|Se impostato a Yes l'icona è assunta dall'oggetto. |
| Icon|Percorso icona browser|Percorso pubblico dell'icona da associare all'oggetto. |
| 


**A29.RUL**Regola di applicazione
Permette di impostare delle regole di applicazione di specifici attributi all'oggetto.
Le varibili utilizzabili devono essere definite nel contesto LOA29.
L'oggetto da porre sulla mappa viene identificato dalla variabile di contesto K1. (CO.K1)

| Attributo|Significato|Descrizione |
| ---|----|----|
| Txt|Descrizione|Significato del modello |
| Str|Condizione|Descrivere l'espressione, se vera saranno assunti gli attributi sottoelencati. |
| Color|Colore|Colore dell'oggetto sulla mappa (Deve essere il nome del colore scritto in inglese) Si attiva solo se si usa URL statico |
| 

