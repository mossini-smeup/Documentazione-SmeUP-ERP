# Componente Timeline

## Abstract

Componente utlizzato per visualizzare eventi in ordine cronologico.


## Funzionalità
- [Eventi](Sorgenti/MB/DOC/LOCTML_F01)
- [Dinamismi](Sorgenti/MB/DOC/LOCTML_F02)
- [Gruppi](Sorgenti/MB/DOC/LOCTML_F03)
- [Navigazione](Sorgenti/MB/DOC/LOCTML_F04)
- [Personalizzazioni grafiche](Sorgenti/MB/DOC/LOCTML_F05)
- [Visualizzare dati](Sorgenti/MB/DOC/LOCTML_F06)


Il componente timeline e' un grafico interattivo che permette di visualizzare eventi disposti su un asse temporale.
Questi eventi possono avere un'orario di inizio o di fine oppure possono essere dei 'singoli eventi', dei quali si specifica solo la data in cui sono avvenuti.

## Formato dei dati
Questo componente viene alimentato da un xml di tipo matrice.

## Dinamismi
La timeline attualmente gestisce solo l'evento 'dateselect', lanciato quando si preme su un evento della timeline.
Allo scattare del dinamismo, vengono generate tutte le variabili di riga relative all'evento cliccato.

## Schede di esempio
Scheda d'esempio, esclusiva per WebUP

 :  : DEC K(Esempi) D(Sezione specifica per il web) X(F(EXD;*SCO;) 1(V2;JAGRA;TML) 2(MB;SCP_SCH;WETEST_TML)) L(1)
