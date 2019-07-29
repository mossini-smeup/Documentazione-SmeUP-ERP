# I Manuali
I moduli possiedono un manuale pdf. Questi manuali possono essere applicativi, operativi o tecnici

# Dove si trovano
I PDF dei manuali sono depositati sul repository il cui percorso è definito nella variabile SME.DOC, sottocartella DOC_BOK.
Il contenuto dei manuali dei moduli standard non è gestible, tali file vengono prodotti dal laboratorio

# Come installare l'archivio manuali dei moduli standard
I pdf dei manuali sono distribuiti in un file compresso reperibile sul sito Smeup nella sezione download.
## Il download
Dal sito Smeup è possibile scaricare un file (in formato zip) contenente tutte le immagini.
Accedere all'area Download del sito Smeup, posizionarsi su "Download Sme.UP ERP" e successivamente nella sezione "Immagini e documentazione". Il file è DocBok.zip.
[http://www.smeup.com](http://www.smeup.com)
## La configurazione
Nella variabile SME.DOC è definito il  percorso dove vengono cercati i documenti in generale. I manuali di cui stiamo trattando sono ricercati nella sottocartella DOC_BOK.
Nell'impostazione standard essa eredita il proprio valore  dalla variabile SME.HOM (a partire dalla quale si definiscono i vari archivi di risorse esterne). Quindi, se si vuole mantenere l'impostazione standard si dovrebbe modificare SME.HOM ed ottenere di conseguenza la modifica della variabile SME.DOC.
Occorre fare attenzione però che così facendo si ottiene come effetto la modifica di TUTTE le variabili che ereditano il valore di SME.HOM. Diversamente si può modificare SOLO il valore di SME.DOC.
Una volta impostata la variabile va riavviato Looc.UP perché la modifica venga recepita.
## Il ripristino
L'archivio in formato zip va scompattato, ottenendo così la cartella DOC_BOK.
La cartella così ottenuta deve essere posizionata in maniera da coincidere con il percorso ottenuto dalla variabile SME.DOC
