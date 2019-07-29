# C£D - Domande
 :  : DEC T(ST) K(C£D)
## OBIETTIVO
Permettere di catalogare domande generiche a cui si potranno associare risposte e/o gruppi di risposte. Ogni domanda potrà aprire un nuovo gruppo di domande fino ad un massimo di tre livelli.
Si potranno quindi gestire configurazioni di prodotto, schede tecniche relative all'offerta ecc.
## SOTTOSETTORI
I sottosettori permettono di suddividere le domande in gruppi che si devono presentare insieme. In particolare, un gruppo di domande così definito potrà essere associato ad una domanda.
## CONTENUTO DEI CAMPI
 :  : FLD T$C£DX **Forme di presentazione**
Definisce la tipologia della domanda : 

- Altre domande : 
-- 01 Macrodomanda di selezione. La selezione serve solo ad indirizzare le domande successive ma non deve essere memorizzata nell'archivio delle risposte.
-- 02 Collega ulteriori domande. Apre un secondo livello di domande. Tipicamente utilizzato per ripetere più di una volta lo stesso gruppo di domande.
- Scelta Oggetto : 
-- 03 Presenta le quantità.
-- 04 Presenta tutti i dati.
- Risposte come descritte in tabella C£R : 
-- 05 Scelta all'interno di una gamma di risposte preparate.
-- 06 Scelta in una gamma di risposte con variazione dati.
-- 07 Presentaz. di una gamma di risposte su formato iniziale.
- Distinte e legami : 
-- 08 Componenti di distinta - assieme specificato in tabella.
-- 09 Componenti di distinta - assieme derivato da una domanda.
-- 13 Componenti di legami - assieme specificato in tabella.
-- 14 Componenti di legami - assieme derivato da una domanda.
- Regole : 
-- 10 Domanda sotto regola   - risposta singola.
-- 11 Domanda sotto regola   - risposta multipla.
- Parametri : 
-- 12 Selezione di oggetto in base ai parametri di prec.domande.

 :  : FLD T$C£DS **Sottosettore domande collegate**
Gruppo di domande descritte in un altro sottosettore. La domanda rappresenta un raggruppamento di domande che si presenteranno successivamente.
 :  : FLD T$C£DT **Tipo risposta**
Specifica la categoria della risposta. Potremo avere : 

- Risposte catalogate e controllate. Queste risposte sono catalogate in un sottosettore della tabella C£R. Esiste uno specifico programma che tratta tali tipi di risposte. Si veda la documentazione relativa alla tabella C£R.
-- Tipo      = TA.
-- Parametro = C£R.
- Risposte che collegano ad un elenco di oggetti quali : 
-- Articoli.
-- Attrezzature.
-- Modalità di pagamento.
-- Altra tabella a piacere.
Anche per queste esiste un programma di gestione specifico.
-- Tipo      = qualsiasi scelta della tabella *CNTT.
-- Parametro = dipendente dal tipo indicato.
- Risposte controllate da una particolare regola. Queste risposte sono collegate ad una regola e al programma ad essa associato. Si veda la documentazione relativa alla tabella C£T.
-- Tipo      = TA.
-- Parametro = C£Txx (sottosettore).

 :  : FLD T$C£DP **Parametro tipo risposta**
Se indicata una tabella permette di definire il nome di tale tabella.
 :  : FLD T$C£DL **Prefisso risposta / domanda**

- 1.   Risposta. È possibile chiedere al programma di presentare all'interno del gruppo di risposte solo quelle che iniziano con i caratteri indicati. Tale prefisso potrebbe coincidere con il codice della domanda stessa. In tal modo tutte le risposte possono essere catalogate in un unico gruppo.
- 2.   Domanda. Se presente il sottosettore domande collegate, questo campo assume il valore di prefisso domande collegate.

 :  : FLD T$C£DO **Risposta obbligatoria**
Indica che almeno una risposta è obbligatoria. Il programma controllerà tale fatto e presenterà le risposte possibili per tutte le domande a risposta obbligatoria, anche se l'utente non procederà alla selezione.
 :  : FLD T$C£DR **Risposta multipla**
Indica al programma di accettare e catalogare anche più di una risposta a fronte di una domanda.
 :  : FLD T$C£DC **Cartella per documentazione**
Indica il contenuto della documentazione OFFICE/400 a cui l'utente potrà accedere mediante l'opzione opportuna sulla lista.
 :  : FLD T$C£DA **Modo presentazione risposte**

- S = Sintesi. Le risposte si presentano nel formato stesso di richiesta delle domande. Ciò può essere utile per le domande con un numero limitato di risposte.
- Q = Dettaglio nota/quantità/valore. Il formato delle risposte possibili gestisce la nota, la quantità e il valore, in funzione della caratteristica di ogni risposta
- F = Finestra gruppi di domande. Le domande di questo tipo si presentano in una finestra di scelta di gruppi di domande, preliminare ad ogni altra domanda. Tale tecnica si usa in presenza di un numero eccessivo di domande.

 :  : FLD T$C£DD **Gruppo distinta**
Le  risposte che si presentano coincidono con la distinta di un prodotto. Sarà possibile scegliere uno o più dei componenti della distinta stessa.
 :  : FLD T$C£D1 **Condizioni di scelta 1**
Definisce fino a tre caratteristiche di questa domanda. Tali caratteristiche saranno utilizzate come condizionamento per la presentazione a video. Se, ad esempio, separo le domande specifiche di un offerta e quelle specifiche dell'ordine, queste si presenteranno solo nel caso opportuno.
 :  : FLD T$C£D2.T$C£D1 **Condizioni di scelta 2**
 :  : FLD T$C£D3.T$C£D1 **Condizioni di scelta 3**
 :  : FLD T$C£D4 **Modalità di stampa domanda**

- T/b  = TOTALE       completa di commenti
- P    = PARZIALE     senza commenti
- C    = COMMENTI     solo commenti
- N    = NO

 :  : FLD T$C£D5 **Modalità di stampa risposta**

- T/b  = TOTALE       completa di commenti
- P    = PARZIALE     senza commenti
- C    = COMMENTI     solo commenti
- N    = NO

 :  : FLD T$C£D6 **Sezione prezzi di listino**
Indica il valore della tabella C£V da cui dovranno essere ripresi i prezzi. Per comprendere il concetto di "sezione" si veda la documentazione relativa alla gestione listini.
 :  : FLD T$C£D7 **Prezzo obbligatorio**

- S =  Sì
- N =  No

 :  : FLD T$C£D8 **Prezzo non modificabile**

- S =  Sì
- N =  No

 :  : FLD T$C£D9 **Programma specifico**
Indica un programma specifico che viene richiamato al momento della selezione della domanda. Tale programma si occupa di definire i dati caratteristici della risposta in un modo particolare. Ciò può risultare utile per la gestione delle eccezioni. Il programma riceve il codice della domanda da cui è richiamato, pertanto può essere condizionato da uno qualsiasi dei parametri. Tale utilizzo è alternativo alla gestione delle regole descritta sopra nei tipi risposta.
 :  : FLD T$C£DI **Tipo domanda**
Utilizzato per permettere l'accesso a sottogruppi di domande. Sono di particolare interesse i seguenti due tipi : 

- D =  Distinta. La risposta deve essere necessariamente un articolo. L'insieme di tali tipi di risposte potrà essere utilizzato per leggere la distinta configurata.
- O =  Operazione. La risposta deve essere necessariamente una operazione. L'insieme di tali tipi di risposte potrà essere utilizzato per leggere il ciclo dell'articolo.

