## Utilizzo testate come gruppi ciclo
Per codificare cicli (intesi come una sequenza di operazioni) non intestati ad un singolo articolo, ma ad un codice di maggior aggregazione, si opera nei seguente modo.

## Impostazioni tabellari
In tabella BRT si compilano i seguenti campi : 
- Si imposta "P" nel campo Ciclo Alternativo P/S
- Nell'oggetto ciclo si inserisce un codice che tipizza l'anagrafica cicli (ad esempio un articolo di tipo "Ciclo" AR/CIC). La lunghezza di questo oggetto è al massimo di tre caratteri (per essere contenuta nel codice ciclo)
- Si imposta ad '1' il ciclo di gruppo

## Cicli prefissi generici
Si inseriscono le fasi del cliclo generico, intestate al : 
- Tipo ciclo codificato
- Codice Ciclo  :  Oggetto del tipo dichiarato in tabella
- Codice Oggetto  :  Uguale al codice ciclo (impostato automaticamente)

## Associazione cicli - testate
Nell'anagrafica delle testate ciclo si inserisce l'associazione (1-n) tra l'articolo e i suoi cicli ammessi (oggetti intestatari delle fasi)

## Scansione cicli
Nella scansione di produzione dell'articolo di uno specifico ciclo, si assume il ciclo stesso come gruppo ciclo, con conseguente associazione dinamica delle fasi

## Impostazione in ordini di produzione
E' possibile selezionare, dato un articolo, il ciclo tra quelli ammessi, oppure implementare una regola di selezione nel visualizzatore degli ordini.

## Particolarità di scansione
Nelle scansioni del ciclo (£CIR e £CIRDB), se impostato il ciclo prefisso, e non ricevuto alcun valore, viene reperito il ciclo di default passando al programma di selezione i seguenti valori : 
- Data scansione
- Quantità
- Codice da Scandiire
- Configurazione

## Utilizzo ciclo come configurazione
E' possibilie impostare in tabella BRT la posizione del ciclo nella configurazione.
Questo valore viene utilizzato nella scansione logistica :  i materiali possono variare in funzione del ciclo selezionato. Ad esempio, se una macchina è alimentata da rotoli ed un'altra da fogli spezzati, la scelta della macchina induce il componente corretto.
Nella scansione "stand alone" della distinta, bisogna prevedere un comportamento di default, nei criteri di selezione, quando sono vuote le posizioni della configurazione che dovrebbero contenere il ciclo.


## Esempio

Tipo Ciclo "PRE"
Articoli di tipo CIC :  C01, C02

Fasi codificate
Tipo PRE
Codice Ciclo C01
Codice Oggetto C01
Fasi 0010, 0020 ...

Tipo PRE
Codice Ciclo C02
Codice Oggetto C02
Fasi 0011, 0021 ...

Testate ciclo
PRE - A01 - C01
PRE - A01 - C02

In questo modo si collegano i due cicli C01 e C02 all'articolo A01.




