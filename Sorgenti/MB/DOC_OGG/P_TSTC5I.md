# FUNZIONI SU PARTITE

## OBIETTIVI
 Analisi delle partite.

## FUNZIONI/METODI

**- INZ/INF** - Inizializzazione :  serve per inizializzare la routine prima di eseguire la funzione RIT/RIF.
**   - PAR** - Per partita :  le rate verranno ritornate in ordine di data registrazione e raggruppando le rate di dovuto che hanno stessa origine.
**   - SCA** - Per scadenza :  le rate vengono ritornate in ordine di data scadenza/rata origine
**   - DAT** - Per data :  le rate vengono ritornate in ordine di data scadenza per le rate di dovuto e data registrazione per le rate di pagamento.
**- RIT/RIF** - Ritorno :  chiamata a ripetizione, dopo aver eseguito una prima volta la funzione INZ/INF, restituisce le rate della partita. La differenza fra RIT e RIF consiste semplicemente nel fatto che la funzione RIF ritorna anche nel campo £C5IRG una stringa contenente i dati già formattati della partita in base allo schema previsto per la funzione VIS.
**- VIS** - Emette a video una visualizzazione della partita indicata.
**   - PAR** - Per partita :  le rate verranno visualizzate in ordine di data registrazione e raggruppando le rate di dovuto che hanno stessa origine.
**   - SCA** - Per scadenza :  le rate vengono visualizzate in ordine di data scadenza/rata origine
**   - DAT** - Per data :  le rate vengono visualizzate in ordine di data scadenza per le rate di dovuto e data registrazione per le rate di pagamento.
**- SIN** - Ritorna i dati generali della della partita indicata.
**   - RID** - Ridotta
**   - COM** - Completa
**   - ANA** - Solo dati anagrafici

## DATI DI INPUT
**£C5ICN**- Contesto :  se impostato a PRO indica che l'analisi delle partita avviene in ottica di analisi delle provvigioni e che di conseguenza la data rischio deve essere presa come valore di input
**£C5ITR/CR** - Soggetto intestatario della partita
**£C5IDD/ND** - Data/Numero documento della partita
**£C5IPE/CO** - Pertinenza/Condizione :  permettondo di filtrare le rate in base ai flag 01/02)
**£C5IDR** - Data registrazione limite :  se impostata indica il riferimento temporale della situazione della partita
**£C5IAZ** - Azienda :  se impostata verrano analizzate solo le rate dell'azienda indicata, altrimenti verranno analizzate tutte le aziende
**£C5IEZ** - Esercizio limite :  ha un funzionamento simile alla data registrazione limite con la differenza che invece che basarsi sulla data si basa sull'esercizio
**£C5IRP** - Inizializza progressivo :  tra i campi di output c'è un progressivo del saldo, questo può fare riferimento ad una sola partita oppure ad una serie di partite nel caso richiami in successione la £C5I per più partite; se valorizzato il progressivo verrà inizializzato tutte le volte che cambia la partita
**£C5IVP** - Costo partita :  tra i campi di output è possibile far calcolare un determinato costo teorico calcolato in funzione delle dilazioni avvenute nei pagamenti ed al costo del denaro indicato nella tabella C51. I costi sono di tre tipi : 
 * Costo del pagamento :  si basa sul n° dei giorni compresi fra la data documento e la data scadenza
 * Costo del ritardo :  si basa sul n° dei giorni compresi fra la data scadenza e la data di pagamento o la data di rifemento nel caso in cui la rata sia ancora aperta
 * Costo incasso :  è dato dalla sommatoria dei precedenti due valori
**£C5ISR** - Filtro sulle ritenute :  se valorizzato indica di escludere dalla partita gli importi relativi alle ritenute attuate sui soggetti
**£C5IGP** - Gruppi partite :  se valorizzato le partite verranno presentate in modo che risaltino i collegamenti che esistono fra partite positive e negative (fatture/note d'accredito) :  tali collegamenti vengono determinati in funzione del fatto che le rate della partita positiva e quelle di una rata negativa abbiamo le rispettive rate di pagamento associate alla stessa riga di registrazione (con una riga ho cioè chiuso sia la fattura che la nota). In questi casi con attivato tale flag al posto delle rate di pagamento verrà indicato il riferimento alla rata della partita di segno opposto che è stata chiusa.
**£C5IVC** - Valuta di conto :  Indica che l'importo da prendere in considerazione non è l'importo in valuta ma l'importo in valuta di conto.
**£C5IIN** - Esclusione insoluti :  indica che dovranno essere escluse dalla scansione le rate relative ad un insoluto.

## DATI DI OUTPUT
Dati di riferimento della partita : 
**£C5IT1** :  Totale rate di dovuto in valuta di conto della partita
**£C5IT2** :  Totale rate di pagato in valuta di conto della partita
**£C5IT3** :  Totale saldo in valuta di conto della partita
**£C5IT4** :  Totale rate di dovuto in valuta della partita
**£C5IT5** :  Totale rate di pagato in valuta della partita
**£C5IT6** :  Totale saldo in valuta della partita
**£C5IH1** :  Totale rate in rischio in valuta di conto della partita
**£C5IH2** :  Totale rate in rischio in valuta della partita
**£C5IP1** :  Totale progressivo rate di dovuto in valuta di conto della partita
**£C5IP2** :  Totale progressivo rate di pagato in valuta di conto della partita
**£C5IP3** :  Totale progressivo saldo in valuta di conto della partita
**£C5IP4** :  Totale progressivo rate di dovuto in valuta della partita
**£C5IP5** :  Totale progressivo rate di pagato in valuta della partita
**£C5IP6** :  Totale progressivo saldo in valuta della partita
**£C5IV3** :  Costo del ritardo in valuta di conto della partita
**£C5IV4** :  Costo del ritardo in valuta della partita
**£C5IS3** :  Costo del pagamento in valuta di conto della partita
**£C5IS4** :  Costo del pagamento in valuta della partita
**£C5IDH** :  Data limite del rischio
**£C5IDU** :  Data ultimo pagamento dell partita

Dati della singola rata :  Record della rata
**£C5IRG** :  Stringa formatta dei dati della rata (se funzione RIF)
**£C5IR1** :  Residuo singola rata di dovuto in valuta di conto
**£C5IR2** :  Residuo singola rata di dovuto in valuta
**£C5IM1** :  Importo singola rata di dovuto in valuta di conto
**£C5IM2** :  Importo singola rata di dovuto in valuta
**£C5IDT** :  Data scadenza del dovuto se rata di pagato
**£C5IGR** :  GG del ritardo
**£C5IV1** :  Costo del ritardo in valuta di conto della singola rata
**£C5IV2** :  Costo del ritardo in valuta della singola rata
**£C5INR** :  N° Record della singola rata
**£C5IVL** :  Codice valuta
**£C5IGT** :  GG del pagamento
**£C5IS1** :  Costo del pagamento in valuta di conto della singola rata
**£C5IS2** :  Costo del pagamento in valuta della singola rata

 Dati il cui significato varia a seconda che sia stia analizzando la partita (sintesi) o la rata (ritorno) : 
**£C5IPH** :  Rischio del pagamento (singola rata o di almento una rata della partita se sintesi)
**£C5IA1** :  Importo abbuoni in valuta di conto (singola rata o totale se sintesi)
**£C5IA2** :  Importo abbuoni in valuta (singola rata o totale se sintesi)
**£C5IES** :  Esito rata (della singola rata o di almeno una rata della partita se sintesi)
