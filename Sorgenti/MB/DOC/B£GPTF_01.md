# Obiettivo

Facilitare il processo di distribuzione di uno o più gruppi di programmi dal laboratorio di sviluppo all'utente finale. Attraverso la scheda viene gestito sia il trasferimento estemporaneo di gruppi sorgenti (DST) che la ricezione e installazione di PTF. All'interno del presente documento con la definizione di Gruppi si farà indistintamente riferimento a DST e PTF.



# Utilizzo

Il trasferimento dei sorgenti avviene tramite due fasi principali, riconducibili alle voci di menù
* 'I-Invio'  ( Preparazione e spedizione dei file da inviare )
* 'R-Ricezione' ( Ricezione e restore degli oggetti ricevuti )	

## Preparazione e spedizione dei file
La preparazione dei sorgenti da trasferire ha inizio con la creazione di uno Script  definito all'interno del file SCP_PTF (la libreria è libera). Il membro che definisce lo script deve essere nominato come STipoGruppo_XXYYY dove il Tipo gruppo sarà compilato con DST o PTF a seconda della tipologia di trasferimento, XX indica l'applicazione di riferimento del gruppo trasferito e YYY è un progressivo libero. La creazione del membro può essere eseguita direttamente dalla scheda selezionando il tab Azioni e quindi 'Crea nuovo script'. Verranno quindi richiesti libreria e nome del membro (il file è fissato a SCP_PTF) .
All'interno del membro, la sintassi dello script è la seguente : 
           :  : DST.MBR Lib="Libreria" Fil="File"
 In questo modo vengono inclusi tutti i Membri Sorgente contenuti in Libreria/File
E' possibile filtrare i Membri con la tecnica inclusione/esclusione come di seguito indicato : 
           :  : DST.MBR Lib="Libreria" Fil="File" Nam="ABC*"
           :  : DST.MBR Lib="Libreria" Fil="File" Nam="*ABC*"
           :  : DST.MBR Lib="Libreria" Fil="File" Nam="*ABC"

Esempio di script : 
 :  : DEC T(MB) P(SCP_PTF) K(SDST_B£002)

###   I - Invio
Una volta creato lo script questo comparirà all'interno delle sezioni 'Gruppi di Distribuzione' / 'Gruppi di Ptf' e  sono disponibili le seguenti azioni : 
 * Crea nuovo script
 * Visualizza Script del Gruppo
 * Modifica Script del Gruppo
 * Cancella Script del Gruppo :  rimuove il membro dal file SCP_PTF
 * Lista dei membri :  visualizza il dettaglio dei membri contenuti nel gruppo
 * Esegui Upload del Gruppo
 * Apri Directory Upload

Terminata la fase di creazione del gruppo si passa al suo trasferimento che esegue un invio dei gruppi ad un Server pubblico.
Per eseguire il caricamento,  selezionare l'azione 'Esegui Upload del Gruppo'.
 Attraverso l'upload verrà creato un savf.

Nel caso il nome del gruppo contenesse il carattere '£', questo verrà sostituito col carattere '_'

## Ricezione ed estrazione del gruppo
La seconda fase del trasferimento di sorgenti viene eseguta dalla sezione 'R - Ricezione'.

###   D - Gestione Download
Si compone di una sezione in cui viene visualizzata la cartella FTP del server pubblico (che contiene i gruppi disponibili e quindi scaricabili sull'I-series di destinazione ) e 2 sezioni con i Gruppi già scaricati
Per scaricare un gruppo selezionare il pulsante 'Esegui Nuovo Download' e indicare il nome del gruppo da scaricare. Attraverso il download verrà generato un savf all'interno della libreria SMEPTF che avrà lo stesso nome dello script che definisce il gruppo ( Salvo l'eccezione della sostituzione del carattere '£' di cui sopra ).

###   R - Ripristino Gruppi
Al termine del download il gruppo scaricato sarà visibile nella sezione 'Gruppi scaricati' e su di esso saranno disponibili le seguenti azioni : 
 * Visualizza Contenuto
 * Esegui Ripristino Oggetti con Creazione/Ricreazione Libreria

Il ripristino del gruppo esegue un restore dell'oggetto all'interno di una libreria che avrà lo stesso nome del savf (e quindi del gruppo) .

###   A - Allineamento Sorgenti
Si compone di una sezione che permette l'analisi delle differenze tra Sorgenti (Origine PTF / Origine Ambiente).Fare riferimento alla Documentazione Operativa
Sono disponibili le seguenti azioni : 
 * Esegui Comparazione
 * Copia Sorgente PTF in Ambiente
 * Compila Sorgente Ambiente

###   E - Eliminazione File/Librerie di Lavoro
Sono disponibili le seguenti azioni : 
 * Elimina Libreria
 * Elimina SAVF

