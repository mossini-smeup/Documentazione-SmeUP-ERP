# C£G - Definizione Archivi
 :  : DEC T(ST) K(C£I)
## OBIETTIVO

## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Codice
E' il nome dell'archivio gestito
 :  : FLD T$DESC Descrizione

 :  : FLD T$RISA Struttura risalita
Indica i livelli di risalita gestiti nell'archivio in esame.  I livelli di risalita sono al massimo nove e in questo
campo si specifica il numero e l'ordine. I campi gestiti nella risalita sono definiti nella tabella C£G con l'elemento
specificato in T$CODR (Codice definiz. ris.).
I nove caratteri del campo rappresentano le nove risalite. Ogni posizione determina una combinazione possibile (vedi
sotto) e deve essere inserito il codice della risalita stessa (1/9).

Esempio classico :       '100200300'

                       Significa che la risalita '1' è quella della posizione 1, la risalita '2' quella della posizione 4
                       la risalita '3' quella della posizione 7.

Le posizioni sono le combinazione degli elementi della tabella C£G e hanno il seguente significato

            **Campo Orizzontale    **Campo Verticale
**Pos1**       Campo 1                 Campo 1
**Pos2**       Campo 2                 Campo 1
**Pos3**       Campo 3                 Campo 1
**Pos4**       Campo 1                 Campo 2
**Pos5**       Campo 2                 Campo 2
**Pos6**       Campo 3                 Campo 2
**Pos7**       Campo 1                 Campo 3
**Pos8**       Campo 2                 Campo 3
**Pos9**       Campo 3                 Campo 3


