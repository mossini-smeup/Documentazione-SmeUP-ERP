# Obiettivo
Con questa routine si recuperano le informazioni e quindi le DS delle tabelle collegate ad una riga

# Funzioni e metodi
_1_Funzioni e _5_Metodi
 * _1_A,        Fino al modello documento
 * _1_B,          ,,    tipo riga
 * _1_C,          ,,    parametro c/lavoro
 * _1_D,          ,,    tipo impegno Materiali
 * _1_E,          ,,    tipo impegno Risorse

Nella £FUNP1/K1 viene passata la riga in esame e nei campi £V5LIR=Tipo riga e £V5LIM=Modello documento si possono passare i rispettivi campi impedendo al programma il recupero (rispettivamente chain sul v5rdoc e v5tdoc).

Nei campi £V5LL1,£V5LL2,£V5LL3  se imposta il codice relativo alla tabella che si vuole come risultato. I codici sono : 
 ** 1   Leggere tabella Tipo Doc. (V5D)
 ** 2   Leggere tabella Mod. Doc. (V5A)
 ** 3   Leggere tabella Tipo Riga (V5B)
 ** 4   Leggere tabella Par.C/Lav (V5L)
 ** 5   Leggere tabella Tipo Imp. (P5I)
 ** 6   Leggere tabella Tipo Imp. (P5S)
e vanno impostati in funzione del campo "funzione". Ricordiamo che la v5d e la v5a sono legate alla testata e che le altre sono legate alla riga.

# Input
I dati di input oltre alla funzione e metodo sono i codice della riga documento in £FUNP1/£FUNK1 i codici delle tabelle richieste e in maniera facolatativa il tipo riga ed il modello documento.

# Output
La routine restituisce al programma chiamante la DS £V5LDS che oltre ai codici specifici (tipo riga,modello e altri) torna nei campi £V5LT1/D1 £V5LT2/D2 £V5LT3/D3 il contenuto e la descrizione delle tabelle richieste che dovranno essere messe nel DS delle tabelle richieste. Esempio se nel campo £V5LL1 è stato inserito il codice '1' nel campo £V5LD1 ci sarà la descrizione della tabella V5D e nel campo £V5LT1 il suo contenuto che nel pgm richiamante andrà messo nella DS V5D$DS

# Prerequisiti
Prerequisiti per l'utilizzo della routine sono le /copy : 
£FUNDS1
£V5LDS

# Esempio di chiamata
>       C                  EVAL  £V5LFU='E'
       C                  EVAL  £V5LME=''
       C                  EVAL  £FUNP1=R§TDOC
       C                  EVAL  £FUNK1=R§NDOC+%EDITC(R§NRIG : 'X')
       C                  EVAL  £V5LL1='2'
       C                  EVAL  £V5LL2='3'
       C                  EVAL  £V5LL3='5'
       C                  EXSR  £V5L
       C                  EVAL  V5A$DS=£V5LT1
       C                  EVAL  V5B$DS=£V5LT2
       C                  EVAL  P5I$DS=£V5LT3


# Note particolari
