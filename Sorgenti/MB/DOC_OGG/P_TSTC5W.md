# FUNZIONI SU SCADENZE

## OBIETTIVI
 Analisi delle scadenze.

## FUNZIONI/METODI
**- INZ -**  Inizializzazione :  serve per inizializzare la routine prima di eseguire la funzione RIT
**   - SCA -**  Scadenzario (ritorna solo le rate aperte)
**   - RIS -**  Rischio (ritorna solo le rate chiuse, ma in rischio)
**   - ESP -**  Esposizione (ritorna sia lo scadenzario che il rischio)
**- RIT -**  Ritorno :  chiamata a ripetizione, dopo aver eseguito una prima volta la funzione INZ, permette restituisce a seconda del metodo le scadenze pendenti o i soggetti con scadenze pendenti
**   -     -**  Vengono ritornate le scadenze
**- INI -**  Inizializzazione :  serve per inizializzare la routine prima di eseguire la funzione LET. E' del tutto speculare alla funzione INZ se non che per INI la scansione sarà SQL.
**   - SCA -**  Scadenzario (ritorna solo le rate aperte)
**   - RIS -**  Rischio (ritorna solo le rate chiuse, ma in rischio)
**   - ESP -**  Esposizione (ritorna sia lo scadenzario che il rischio)
**- LET -**  Ritorno :  chiamata a ripetizione, dopo aver eseguito una prima volta la funzione INI, permette restituisce a seconda del metodo le scadenze pendenti o i soggetti con scadenze pendenti. E' del tutto speculare alla funzione RIT se non che per INI la scansione sarà SQL.
**   -     -**  Vengono ritornate le scadenze

### DATI DI INPUT
**£C5WTR/CR** :  va indicato l'oggetto di riferimento della scansione. Per le funzioni
INZ/RIT è ammesso solo un oggetto CN, mentre per le funzioni INI/LET sono ammessi gli oggetti : 
* CN o LICN
* D8*YYMD o LID8*YYMD (Intesa come Data Scadenza)
* TAAGE o LITAAGE (Inteso come Responsabile del Credito)
* TAC5F o LITAC5F
* V2C5TSC
* AZ
**£C5WAZ** :  Azienda (se impostata verrano analizzate solo le rate dell'azienda indicata, altrimenti verranno analizzate tutte le aziende)
**£C5WPE/CO** :  Pertinenza/Condizione (permettondo di filtrare le rate in base ai flag 01/02)
**£C5WDR** :  Data registrazione limite (se impostata indica il riferimento temporale della situazione delle scadenze. ATTENZIONE!!! se impostato questo parametro comporta un certo appesentimento dell'elaborazione in quanto dovranno essere elaborate tutte le rate del soggetto e non solo quelle in scadenza ad oggi...)
**£C5WDK** :  Data rischio (se impostata indicata la data da prendere a riferimento al posto della data odierna nella determinazione delle rate a rischio)
**£C5WFR** :  Filtro ritenute (se impostato fa in modo che gli importi ritornati dalla routine non tengano conto della parte relativa alle ritenute)
**£C5WLC** :  Livello chiamata

### DATI DI OUTPUT
**Record della rata**
 I campi seguenti esistono in quanto questi permettono di riportare i valori dei campi del record che possono essersi modificati nel tempo nel caso in cui abbia impostato la data registrazione limite :  esempio l'importo in scadenza oggi (riportato sul record della rata) può essere differente dall'importo in scadenza alla data registraz. limite impostata (riportato nell'apposito campo di output). Perciò tendenzialmente in analisi bisognerebbe tener conto dei valori delle variabili di output invece che dei relativi campi del record.

**£C5WIV** :  importo in scadenza in valuta
**£C5WIM** :  importo in scadenza in valuta di conto
**£C5WTP** :  tipo protocollo
**£C5WNP** :  numero protocollo
**£C5WDP** :  data pratica

 Questi campi vengono invece ritornati quando analizzati i soggetti aventi rate in scadenza.
**£C5WTO** :  Tipo Contatto
**£C5WCO** :  Codice Contatto
