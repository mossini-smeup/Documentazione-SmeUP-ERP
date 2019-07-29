# CRJ - Tipo Ciclo Di Collaudo
 :  : DEC T(ST) K(CRJ)
## OBIETTIVO
Questa tabella guida alla definizione dei tipi di ciclo di collaudo della relativa struttura
## Come funzionano le risalite
 La risalita avviene in questo modo : 
  -1- Dato il tipo ciclo definito in tab CQL si valorizzano le chiavi con i valori del lotto. Si cerca il ciclo di quel tipo con quelle chiavi.
Il modo con cui si valorizzano le chiavi è definito (cablato) nel pgm B£ICQC0. Se, ad esempio, la prima chiave della griglia è AR, il pgm B£ICQC0 sostituisce al primo codice il valore dell'articolo del lotto (T$ARTI); se la chiave è CN-FOR verrà sostituito l'ente di addebito (T$COEA)... ecc...
  -2- Se non viene trovato un ciclo con queste chiavi, si sostituisce il valore generico (**) alle chiavi e si cerca questo stesso tipo ciclo con le nuove chiavi.
  -3- Se non viene ancora trovato si provano a sostituire i valori dei rispettivi OAV (impostati in tab CRJ) alle chiavi e si cerca il tipo ciclo di risalita (T$CRJK) con queste nuove chiavi.
  -4- Se non viene ancora trovato si sostituisce il valore generico (**) alle chiavi.
  -5- Se non trovato si ricomincia da capo, provando le risalite tramite gli OAV definiti nel tipo ciclo di risalita. In pratica si percorre una catena di elementi della CRJ, continuando a sostituire alle chiavi i valori dell'OAV e cercando il ciclo del tipo def in T$CRJK .
_7_Attenzione a non creare un loop infinito!
 N.B. Se nei campi T$CRJD,T$CRJG o T$CRJJ al posto dell'OAV scrivo 'STOP', quando faccio una risalita su un nuovo tipo ciclo il relativo codice, non viene riportato (viene perso).
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice Tipo Ciclo di Collaudo**
 :  : FLD T$DESC **Descrizione**
 :  : FLD T$CRJA **Tipo Griglia**
È un elemento della tabella B£G. Definisce gli oggetti del Ciclo di Collaudo
NB. Se previsti in griglia gli oggetti sono obbligatori anche se non indicato espressamente dall tab. B£G, in caso non si
    voglia specificare un valore preciso usare i caratteri "**".
 :  : FLD T$CRJD **OAV Risalita 1**
Leggere all'inizio di questo documento come funzionano le risalite sugli OAV.
Inserire l'OAV del primo oggetto della griglia definita in T$CRJA
 :  : FLD T$CRJG **OAV Risalita 2**
Leggere all'inizio di questo documento come funzionano le risalite sugli OAV.
Inserire l'OAV del secondo oggetto della griglia definita in T$CRJA
 :  : FLD T$CRJJ **OAV Risalita 3**
Leggere all'inizio di questo documento come funzionano le risalite sugli OAV.
Inserire l'OAV del terzo oggetto della griglia definita in T$CRJA
 :  : FLD T$CRJK **Tipo Ciclo Risalita**

 :  : FLD T$CRJL **Suffisso Programma Aggiustamento**
Se si desidera utilizzare un programma particolare di calcolo valori, è possibile specificare il suffisso del programma da richiamare. Se presente un valore diverso da ' ' , viene lanciato il programma di aggiustamento. 'CQCM50_x'. Per maggiori informazioni sulla modalità di utilizzo del programma leggere le note riportate nel sorgente del programma prototipo (CQCM50_X).
 :  : FLD T$CRJM **Categoria parametri interni**
È un elemento della tabella C£I. Definisce come sono gestiti i parametri che descrivono i campi liberi (5 alfanumerici e 5 numerici), contenuti nell'archivio Cicli Collaudo di questa tipologia.
 :  : FLD T$CRJN **Dati Camp./articolo**
Abilita o meno la gestione dei dati caratteristici dei Piani di Campionamento (Piano/Livello Collaudo, L.Q.A.)
 :  : FLD T$CRJR **Solo 1 Documento**
Nella gestione dei rilievi di collaudo utilizza sempre lo stesso numero documento
 :  : FLD T$CRJS **Suffisso programma Controllo**
È il suffisso del pgm CQCM50D_x che permette di gestire controlli e aggiornamenti specifici in fase di gestione del file (es. CQCM50D_X).
