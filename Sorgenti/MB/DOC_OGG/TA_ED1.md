# ED1 - Tabella personalizzazione
## OBIETTIVI
Definire una descrizione ed un indirizzo dell'azienda titolare del sistema origine. Possibilità di attivare la gestione degli scenari (files multimembro)
## SOTTOSETTORI
Non gestiti
## INTRODUZIONE
Tabella a elemento fisso
## CONTENUTO DEI CAMPI
 :  : FLD T$DESC Descrizione
 :  : FLD T$ED1A __Indirizzo azienda__
Nome di riferimento azienda origine (mittente), definito da un tipo oggetto TA tabella EDI.
 :  : FLD T$ED1B __Attivazione scenari__
Impostando 2(SI attivazione scenari) può gestire nella stessa applicazione più sistemi informativi attraverso l'utilizzo di files multimembro.
 :  : FLD T$ED1C __Destinatari mail log__
Definisce il percorso di memorizzazione del file IFS contenente i destinatari delle mail di monitoraggio della trasmissione EDI outbound (esempio ddt e fatture).
Un percorso di esempio potrebbe essere /Smedoc/mailing/EDI_out.txt
Il file deve essere un file di testo semplice, contenente per ogni riga un indirizzo mail di destinazione.
La mailing list qui definita viene usata durante la trasmissione di file edi outbound nei seguenti casi : 
- in caso di errore di trasmissione, per l'opportuna segnalazione al personale responsabile
- in caso di attivazione log sul cliente (parametri £ED oggetto CNxxx), per il monitoraggio   dei clienti in fase di avvio
