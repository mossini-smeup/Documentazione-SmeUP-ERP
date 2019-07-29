# M5V - Guida rilascio M5 - V5
## OBIETTIVI
Descrivere le modalità con le quali viene eseguito il rilascio del consiglio di pianificazione verso l'ambiente del ciclo esterno. L'elemento di questa tabella va inserito, insieme con il programma di rilascio (M5PNV5_SM), nel parametro suggerimento della fonte pianificata, assegnata al consiglio tramite la politica di pianificazione.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$M5VA __Tipo documento__
È un elemento della tabella V5D. È un campo obbligatorio :  definisce il tipo documento che intesta il documento d'arrivo.
 :  : FLD T$M5VB __Modello documento__
È un elemento della tabella V5A. Se impostato, deve appartenere al sottosettore definito nel tipo documento.
In caso di inserimento di un nuovo documento, esso sarà di questo modello. Se non impostato verrà assunto il modellodocumento di default presente nel tipo documento.
In caso di accodamento, se impostato sarà una condizione per l'accodamento, se non impostato non verrà eseguito nessun controllo (l'accodamento avverrà sul primo documento che soddisfa le rimanenti condizioni, non sul modello documento di default).
 :  : FLD T$M5VC __Tipo riga__
È un elemento della tabella V5B. Se impostato, deve appartenere al sottosettore definito nel modello documento, se impostato anche questo, o a quello del modello documento di default, se non impostato.
Definisce il tipo riga che assumerà la riga del documento generata.
Se non impostato, verrà assunto il tipo riga di default del modello documento, se impostato anche questo, o quella del modello documento di default, se non impostato.
 :  : FLD T$M5VD __Modo accodamento__
È un elemento fisso V2/M5AV5. Definisce le modalità che guidano la scelta se accodare o meno la riga ad un documento esistente o intestare un nuovo documento. Riferirsi all'aiuto specifico di questo oggetto per un'esposizione dettagliata dei vari modi di accodamento.
 :  : FLD T$M5VE __Stato per accodamento__
Se il modo di accodamento è secondo lo stato, definisce lo stato massimo a cui può essere la testata del documento, a cui la nuova riga può essere accodata.
 :  : FLD T$M5VF __Gestione commessa__
Se impostato, nell'applicazione "suggerimento con variazioni", viene presentata la commessa con possibilità di modificarla
 :  : FLD T$M5VG __Passa a testata__
Se impostato, nell'applicazione "suggerimento", dopo che è stata scritta una testata, si passa in modo automatico alla sua variazione
 :  : FLD T$M5VH __Passa a riga__
Se impostato, nell'applicazione "suggerimento", dopo che è stata scritta una riga, si passa in modo automatico alla sua variazione
 :  : FLD T$M5VI __Trattamento plant associato__
Definisce la modalità con cui vengono riempiti i campi del magazzino e del magazzino di trasferimento, a partire dai campi del magazzino e del magazzino associato, presenti nel consiglio di pianificazione che si sta rilasciando.
**NB** :  le considerazioni seguenti valgono sia per campi della riga sia per quelli della testata (qualora essa venga scritta)
Questo campo può assumere i seguenti valori : 
_7_' ' :  Si trasferisce il magazzino del consiglio nel magazzino del documento. Questo è anche il coportamento che viene assunto se è assente nel consiglio il magazzino associato, indipendentemente dal valore del presente campo.
_7_'A' :  Si trasferisce il magazzino del consiglio nel magazzino di trasferimento del documento. Si trasferisce il magazzino associato del consiglio nel magazzino del documento. Si consiglia di impostare questo valore quando si segue il modello standard di trasferimento.
_7_'B' :  Si trasferisce il magazzino associato del consiglio nel magazzino del documento.
_7_'C' :  Si trasferisce il magazzino del consiglio nel magazzino del documento. Si trasferisce il magazzino associato del consiglio nel magazzino di trasferimento del documento.
 :  : FLD T$M5VJ __Stato annullamento__
Se impostato definisce lo stato in cui viene posta la riga del documento in caso di applicazione di un
suggerimento di annullamento.
Se questo campo non è impostato, l'applicazione di un suggerimento di annullamento cancellerà fisicamente
il record della riga del documento.
 :  : FLD T$M5VK __Congruenza Plant__
Se impostato, nell'applicazione "suggerimento", i plant che assumerebbe la riga, saranno utilizzati come vincoli per l'accodamento ad una testata esistente.
