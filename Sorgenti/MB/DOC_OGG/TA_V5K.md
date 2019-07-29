# V5K - Tipo KIT
 :  : DEC T(ST) K(V5K)
## OBIETTIVO
Definisce le caratteristiche relative ai tipi di KIT
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
Indica il codice del KIT
 :  : FLD T$DESC Descrizione
 :  : FLD T$V5KA Tipo aggr. capo
Definisce il valore del FLAG 11 della riga padre del kit : 

- A         Solo descrittivo : 
- B         Rilevanza disponibilità :  Il codice capo del Kit viene movimentato a
            magazzino
- C         NON rilevanza disponibilita' :  il codice capo del Kin NON viene movimentato
            a magazzino

In fase di creazione di una riga documento nel flag 11 di riga del capo
verranno forzati i valori ripresi dalla tabella del tipo kit corrispondente.
 :  : FLD T$V5KF Calcolo prezzo capo
Definisce il valore del FLAG 29 della riga padre del kit : 

- 3         Prezzo derivato dai componenti
- 4         Prezzo forzato a 0
- X         Assunto da V5B
In fase di creazione di una riga documento nel flag 29 di riga del capo
verranno forzati i valori ripresi dalla tabella del tipo kit corrispondente.

 :  : FLD T$V5KB Tipo aggr. riga
Definisce il valore del FLAG 11 delle righe componenti del kit : 

- M         Solo descrittivo
- N         Rilevanza disponibilità :  Il codice componente del Kit viene movimentato
            a magazzino
- O         NON Rilevanza disponibilità :  Il codice componente del Kit NON viene
            movimentato a magazzino

In fase di creazione di una riga documento nel flag 11 di riga del componente
verranno forzati i valori ripresi dalla tabella del tipo kit corrispondente.
 :  : FLD T$V5KG Calcolo prezzo componenti
Definisce il valore del FLAG 29 delle righe componenti del kit : 

- 3         Prezzo derivato dai componenti
- 4         Prezzo forzato a 0
- X         Assunto da V5B

In fase di creazione di una riga documento nel flag 29 di riga del componente
verranno forzati i valori ripresi dalla tabella del tipo kit corrispondente.
**NB**
Nel caso delle righe componenti il valore 3, presente per omogeneita' con lo stesso campo del
capo, non e' consentito.
 :  : FLD T$V5KC SS tipo riga figlio
Sottosettore della V5B che contiene il tipo riga da usare in fase di generazione delle righe
componenti del KIT
**NB**
La funzione di inizializzazione delle righe documento (£V5Z) assume che il tipo riga da generare
sia contenuto nel sottosettore della tabella V5B specificato nel modello del documento che si sta
trattando.
Ne consegue che il il sottosettore qui specificato serve solo per meglio individuare il campo
successivo (tipo riga), si consiglia fortemente di verificare la congruenza tra questi dati e
quelli specificati nel documento che si vuole gestire con questo tipo Kit.
 :  : FLD T$V5KD Tipo riga figlio
Tipo riga da usare in fase di generazione delle righe dei componenti del KIT
**NB**
A prescindere dal gruppo flag specificato in questo tipo riga il valore del FLAG11 verra' impostato
con quanto specificato nel campo "tipo aggregazione riga" di questa tabella
 :  : FLD T$V5KE Suff. pgm controllo
la valorizzazione di questo campo determinera' la chiamata ad un programma V5FUKIT_x dove x e'
il suffisso specificato.
Questa chiamata viene effettuata nell'ambito dell'esecuzione del programma V5FUKIT che si occupa
di svolgere le funzioni delle righe documento KIT.
 :  : FLD T$V5KH Tipo Riga RIM per rilevanza disponibilita'
Tipo riga RIM da usare in fase di creazione delle RIM da documento (V5AT15E) per le
righe documento che hanno rilevanza disponibilita'.
 :  : FLD T$V5KI Tipo Riga RIM per NON rilevanza disponibilita'
Tipo riga RIM da usare in fase di creazione delle RIM da documento (V5AT15E) per le
righe documento che NON hanno rilevanza disponibilita'.
Queste righe non devono effettivamente movimentare alcunche' ma vengono create comunque
per garantire l'integrita' della struttura del KIT durante la fase di evasione e di generazione
della bolla.
Si consiglia di usare un tipo riga RIM (TA GMZ) con impostati i seguenti campi : 
- Causale assunta 1           Blank
- Causale assunta 2           Blank
- Livello di nascita          8
- Prel/Vers/Trasferim.        L  (Libera :  nessun prelievo/versam )

in modo che la riga non abbia impatto su nessun tipo di movimentazione
