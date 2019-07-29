# OBIETTIVO
Tramite questo servizio è possibile ottenere la costruzione dinamica del documento XML.
Per ottenere il documento XML si devono uttilizare i Nodi appartenenti alla stessa struttura.

# PARAMETRI DI INPUT
* £J15FU :  Funzione
* £J15ME :  Metodo
* £J15DS :  Immagine di Comunicazione
* £J15IM :  Immagine di Input/Output
* £J15MS :  Codice Messaggio
* £J15FI :  File Messaggio
* £J1535 :  Errore

## Immagine di comunicazione
Vediamo in dettaglio i parametri di comunicazione
* £J15CO - Contesto, insieme alla struttura identifica il documento XML
* £J15ST - Struttura, insieme al contesto identifica il documento XML
* £J15TN - Tipo nodo, permette di derivare il nodo da una struttura conosciuta : 
** "M"     "Messaggi.Messaggio"
** "MO"    "Opzioni.Opzione"
** "GC"    "Griglia.Colonna"
** "SP"    "Setup.Program"
** "EX"    "Setup.Program"
** "EXB"   "EXB"
** "EXBS"  "Setup"
** "EXBU"  "UserSetups"
** "EXBUS" "Setup"
** "EXUA"  "EXU.Actions"
** "EXUCO" "EXU.Comandi.Oggetto"
** "EXUS"  "EXU.Config"
** "EXUFF" "EXU.Fields.Field"
** "EXUR"  "EXU.Search"
** "U"     "UserSetups"
** "US"    "Setup"
* £J15ND Permette la creazione di un nodo non presente nei tipi nodi
* £J15AP Non chiudere il nodo se in presenza di uno stesso nodo
* £J15SA Nodo senza attributi

# FUNZIONI E METODI
## CON.CRE - Contesto Crea
Prima di iniziare a memorizzare i nodi del documento XML bisogna creare il contesto impostando i
campi £J15CO e £J15ST.
## NOD.CRE - Nodo Crea
Attraverso questo metodo si creano i nodi del documento XML.
La profindità del documeto XML è data dalla profondità del tipo nodo stesso.
Attraverso l'immagine è possibile passare gli attributi del nodo.
Il tipo nodo è obbligatorio, se non definito, bisogna rispettarne comunque la sequenzialità e la
profondità ed impostarne il valore nel nodo.
## RIT.XML - Ritorna il documento XML
Attraverso questo metodo viene ritornato il documento in formato XML e svuotato il contesto.

