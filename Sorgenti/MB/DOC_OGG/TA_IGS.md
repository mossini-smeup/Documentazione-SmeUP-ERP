# IGS - Livelli sintesi ind. gestione
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È il codice dell'elemento.
 :  : FLD T$DESC Descrizione
È la descrizione della sintesi.
 :  : FLD T$KYC1 __Codice 1/2/3__
È definito dal tipo oggetto *CNTT, più il relativo parametro, se previsto.
 :  : FLD T$KYC2.T$KYC1 __Codice 2__
 :  : FLD T$KYC3.T$KYC1 __Codice 3__
 :  : FLD T$IGSA __Associa i totali/Gruppo/Prefisso__
È possibile, in fase di estrazione dati, attivare la scrittura automatica di ulteriori livelli di sintesi
_9_Esempio : 
Totalizzazioni per Cliente / Agente / Classe materiale / Cliente-Articolo etc.
L'elenco di tali totalizzazioni è pilotato dal subsettore della tabella IGL. In seconda istanza è possibile estarpolare un sottoinsieme degli elementi della tabella tramite prefisso.
 :  : FLD T$IGSG.T$IGSA __Associa i totali del gruppo__
 :  : FLD T$IGSP.T$IGSA __Associa i totali del prefisso__
 :  : FLD T$IGSB __Associa aggregazione__
Permette, dall'estrazione dati, di attivare automaticamente il calcolo delle aggregazioni tramite la tabella IGG collegata.
 :  : FLD T$IGSC __Aggregazione__
Le aggregazioni possono essere al massimo 9. Verranno utilizzate successivamente per interrogare/stampare i dati, permettendone ordinamenti e/o totalizzazioni.
 :  : FLD T$IGST __Trattamento periodo__
Permette, in creazione della sintesi di totale, di utilizzare il periodo oppure l'esercizio.
'E' = Esercizio cioè 4 posizioni (es. 1999.)
' ' = Periodo                   (es. 199901.)
