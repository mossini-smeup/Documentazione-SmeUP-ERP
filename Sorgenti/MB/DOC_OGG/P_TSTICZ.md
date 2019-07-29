# Obiettivo
Interfacciare il programma in esecuzione con l'anagrafico colli delle diverse applicazioni previste nella tabella di personalizzazioni B£1
Eseguire la ricerca alfabetica relativa se richiesto

# Funzioni e metodi

# Input
£ICZFU :  Funzione
£ICZME :  Metodo
£ICZAM :  Ambiente
£ICZCO :  Contesto
£ICZPA :  Tipo Collo
£ICZCD :  Codice Collo
£ICZRI :  N.ro Record di input

# Output
£ICZCD :  Codice Collo scelta (se eseguita ricerca)
£ICZDE :  Descrizione collo
£ICZMS :  Codice messaggio ritorno (7)
£ICZFI :  File   messaggio ritorno (10)
£ICZCM :  Ultimo Comando
*IN35  :  se On = Codice errato
*IN36  :  se On = eseguita ricerca alfabetica
£ICZRO :  N.ro Record di output

# Prerequisiti
* Dichiarazione della DS per l'utilizzo dell'API all'interno di un programma
D GMCOLL         E DS                  EXTNAME(GMCOLL0F)

# Esempio di chiamata


# Oggetti collegati


# Note particolari

È preferibile eseguire un clear della DS GMCOLL prima di ogni richiamo
