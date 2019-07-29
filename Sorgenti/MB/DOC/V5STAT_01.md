# Introduzione

## Premessa
Il modulo STAT dell'applicazione V5 è dedicato alle statistiche di fatturazione.
Sono gestite le statistiche di fatturato sia sul ciclo attivo che sul ciclo passivo.

## Obiettivo del modulo
Fornire in Sme.Up la funzione delle statistiche disponibile in tutte le sue funzioni di base già pronte, immediatamente utilizzabile, senza alcun intervento da parte dell'installatore.

## File
Il file V5STAT0F è un file estratto dagli archivi transazionali attraverso funzioni specifiche di creazione (ETL), contenente già alcune proprietà di articoli ed enti necessari alle analisi di base, personalizzabile per contenere informazioni specifiche.
I valori sono sommabili algebricamente, per cui una nota di accredito o uno sconto saranno espressi con un valore negativo.
I record con quantità zero e valore diverso da zero, sono movimenti a valore.

## Ripresa
L'estrazione della statistica viene effettuata a partire da 2 file principali : 

 * C5TREG, è il file delle registrazioni contabili che viene scandito per tutte le estrazioni che riguardano il fatturato contabilizzato.
 * V5TDOC, è il file dei documenti del ciclo esterno che viene scandito per tutte le altre estrazioni.

## Struttura del file
Il dettaglio di ogni singola riga della statistica  è dato dalla riga di un documento.
L'oggetto intestatario di una riga può essere un articolo o un oggetto specifico (p.e. spese, sconti, registrazioni contabile,ecc.)
I valori di testata del documento o della fattura vengono appiattiti a livello di riga.

## Documentazione file
Vedi la scheda dell'oggetto File.
 :  : DEC T(OJ) P(*FILE) K(V5STAT0F)

## Analisi della statistica
Una struttura di schede LOOC UP fornisce già gli strumenti di base per la sua analisi.
