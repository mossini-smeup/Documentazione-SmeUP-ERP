# Impostazione
Si basa sul fatto di creare dei codici di _2_Gruppo di fatturazione, attribuendoli ai vari clienti, in modo da formare gruppi di clienti, organizzati per periodicità di fatturazione.
I codici di periodicità di fatturazione vengono catalogati nella tabella**BR*CF** (solo descrittiva) ed assegnati ai clienti mediante l'estensione £08 del BRESCO.

# Lancio stampa periodica
Nel formato di lancio stampa fatture scegliere la modalità :  _2_Fatture a data fissa ed inserire il Gruppo di fatturazione.
Il sistema utilizzerà il gruppo di fatturazione per filtrare i clienti per i quali stampare la fattura.

# Calendario di fatturazione
Si può creare un calendario di fatturazione nel quale impostare le date fisse di fattura per ciascun gruppo creato in precedenza (tab. BR*CF).

Nella tabella**V51**è presente il campo per determinare il calendario di fatturazione, mediante il quale si indica il tipo risorsa di riferimento. Ne è un esempio l'elemento FAT della tabella TRG.

Il calendario di fatturazione, basato sul tipo risorsa definito nella V51, si gestisce come un normale calendario di disponibilità risorse :  per ogni gruppo di fatturazione (elemento di tabella BR*CF) nel calendario si dovranno gestire : 
 * _3_Dati base risorsa, marcare come "festivi" tutti i giorni della settimana
 * _3_Eccezione per risorsa, marcare come "normali" i giorni corrispondenti alle date di fatturazione volute per il gruppo

in altre parole dovrò ottenere una disponibilità risorse nei soli giorni di fatturazione.

La stampa fatture a data fissa utilizzerà la data calcolata dal calendario, quando presente, come ulteriore elemento di filtro (in aggiunta alla data fattura ed al gruppo di fatturazione presenti del formato di lancio).

# Tabelle
## Tabella calendario fatturazione
 :  : DEC T(ST) K(BR*CF) I(·)

## Tabella impostazione tipo risorsa per calendario di fatturazione
 :  : DEC T(TA) P(V51) K(*)

## Tabella tipo risorsa
 :  : DEC T(ST) K(TRG) I(·)
>> esempio tabella TRG da SMETAB
 :  : DEC T(TA) P(TRG) K(FAT) I(elemento)
