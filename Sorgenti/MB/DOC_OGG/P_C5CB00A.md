
# Obiettivo

Trasmissione file all'agenzia delle entrate riguardante la rendicontazione dati nazionali paese per paese (CbCR - DAC4)

Prima di procedere è necessario : 
* Codificare nell'ambiente italiano principale le anagrafiche aziendali interessate. In particolar modo vanno codificate ragione sociale, indirizzo, località, CAP, provincia, partita iva e/o codice fiscale.
* Per le aziende interessate compilare il campo codice attività nella tabella C5H. Se questo campo non viene valorizzato, l'azienda non verrà presa in considerazione. E' possibile richiamare la manutenzione della tabella C5H selezionando dalla schermata "Aziende CBCR"
* Inserire i valori nella categoria parametri £VC con in chiave esercizio e nazione. E' possibile richiamare la manutenzione dei parametri selezionando dalla schermata "Valori per esercizio/nazione"

# Richiesta Parametri

* Azienda tenuta alla comunicazione :   indicare il codice azienda italiana principale tenuta   alla comunicazione
* Esercizio :  indicare l'esercizio a cui fanno riferimento i dati trasmessi.
* Tipologia di invio : 
**   - Invio ordinario - Normale Trasmissione dei Dati.
** A - Annullamento - Trasmissione che annulla  una precedente comunicazione inviata In questo caso bisognerà indicare il progressivo invio da annullare.
* Progressivo per Annullamento :  E' obbligatorio indicare il campo se selezionato annullamento.
* Trasferimento :  mettendo un carattere qualsiasi nel campo, sarà possibile   accedere alla maschera in cui poter indicare il percorso ove verranno depositati i file della   comunicazione da inviare all'agenzia delle entrate.   Il nome dei file verrà composto nel seguente modo :    IT + Esercizio +'-'+CodiceFiscale + Progressivo.XML
* Aziende CBCR :  permette di richiamare in manutenzione la tabella C5H, andando ad indicare   per ogni azienda interessata il campo codice attività CBCR.
* Valori per esercizio/nazione :  permette di richiamare i parametri £VC per indicare i valori   a livello di esercizio/nazione.
* Info aggiuntive :  permette di richiamare le info aggiuntive suddivise per nazione e/o   riferimento ad informazione sommario.
