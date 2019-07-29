# Componente SpreadSheet (SHE)
## Abstract

Il componente SpreadSheet permette di rappresentare i dati su un foglio elettronico e di interagire con lo stesso, modificandolo e downloadandolo. Se vi si associa un servizio i dati possono essere recuperati tramite tale servizio e sempre tramite esso possono essere aggiunti o modificati sul server.



## Dettagli

Per la configurazione del componente è necessario definire un template Excel. Esso va caricato in una posizione accessibile al sistema, ad esempio sul server SERVERX e richiamato con il valore del J1 PATHFILE corrispondente, ad esempio \\SERVERX\smeup\Test\sample.xlsx

Il template Excel può contenere formule, celle colorate, celle con determinati formati (ad esempio data, numerico...), celle readonly e verrà renderizzato dal componente SpreadSheet mantenendo le stesse caratteristiche. Se il template contiene più fogli il componente renderizzerà i vari fogli in una struttura a tab.

La modalità più semplice di utilizzo del componente è quella senza l'associazione ad un servizio server. In questo caso il foglio elettronico renderizzato dal componente SpreadSheet potrà essere modificato online all'interno di Web.UP. Alla conclusione delle modifiche sarà possibile scaricare il file Excel corrispondente contenente quelle stesse modifiche.

L'utilizzo più interessante del componente prevede però l'associazione ad un servizio server. Il servizio deve rispettare il protocollo dell'input panel e della matrice di aggiornamento proprio perchè il foglio elettronico può essere concepito come un input panel (se permette la modifica di un solo record di una matrice dati) o come una matrice di aggiornamento (se permette la modifica di più record di una matrice dati). La configurazione invece di stare in attributi di setup, celle G, colonne di formule, etc... sta all'interno del template Excel. All'interno del template è quindi possibile definire sia la rappresentazione grafica dei dati sia le formule da applicare sui dati. Grazie alla potenza configurativa di un foglio Excel il componente SpreadSheet permette pertanto una maggiore potenza configurativa rispetto a input panel e matrice di aggiornamento.

Per definire dove e come i dati provenienti dal server devono essere mostrati all'interno della renderizzazione dello SpreadSheet è necessario utilizzare all'interno del template Excel un linguaggio di markup ben definito.

Si potrebbe ad esempio voler creare uno SpreadSheet per i budget di progetto. In questo caso si visualizzerebbero solo i dati di un record, come nel caso di un input panel. Per mostrare la descrizione del progetto, che nella matrice dati è individuata dalla colonna PROJ_DES basta scrivere nel template Excel alla posizione desiderata, esempio cella C2 : 

${smeuprow['PROJ_DES'].val}

Questo linguaggio indica che verrà stampato il valore del primo record della matrice dati per la colonna PROJ_DES.

Un dato può essere mostrato formattato, ad esempio come una data o un numero con X decimali, oppure può essere reso readonly. Tutte queste configurazioni possono essere effettuate all'interno del template Excel dando quel formato alla/e cella/e desiderata.
Inoltre tutte le formule scritte nel template (e non solo formule matematiche ma anche concatenazioni o qualsiasi tipo di formule Excel) saranno renderizzate graficamente nel componente SpreadSheet. Ad ogni modifica di un dato il componente si aggiornerà, su tutte le formule.

Oltre a visualizzare solo i dati di un record si possono visualizzare nello SpreadSheet anche i dati di tutta una tabella, ad esempio si potrebbe volere un foglio elettronico che per ogni socio permetta di definire e modificare le quote ad esso attribuite. In questo caso sarà necessario utilizzare all'interno del template (in particolare nel commento di una cella) una scrittura del tipo :  tie : each(items="smeuptable", var="row", length="1") che permette di ciclare su tutte le righe della matrice dati. Il singolo dato si potrà visualizzare come già detto, ovvero con una espressione del tipo : 

${row['PARTNER'].val}

Per maggiori dettagli si rimanda agli esempi. In particolare si consiglia in fase di configurazione del template Excel di scaricare il template Excel associato agli esempi e di osservare come è impostato.

## Funzionalità

- [Caricamento di un xls, modifica e download](Sorgenti/MB/DOC/LOCSHE_F01)
- [Visualizzazione e modifica di un record](Sorgenti/MB/DOC/LOCSHE_F02)
- [Visualizzazione e modifica di più record](Sorgenti/MB/DOC/LOCSHE_F03)
- [Formato delle celle](Sorgenti/MB/DOC/LOCSHE_F04)
- [Dinamismi](Sorgenti/MB/DOC/LOCSHE_F05)

## Formato dati
Tipo di XML utilizzato :  Xml di matrice

## Funzionalità ed attributi
Le funzionalità, le impostazioni e gli attributi del componente sono consultabili attraverso il configuratore e la sua documentazione.

 :  : DEC K(Clicca qui.) D(Apri il configuratore per vedere tutte le possibilità.) X(F(INT;JA_00_01;GES.EDT) 1(RE;L-;EDT_SCH) 2(**;;&AM.LL) 3(OJ;*USRPRF;&AM.UT) 4(**;;DOCSETUP) P(SECLS(G.SET.SHE))) L(1)

## Schede di esempio
Gli esempi del componente sono consultabili sulla sezione specifica per il web : 

 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;SHE) 2(MB;SCP_SCH;WETEST_SHE)) L(1)

