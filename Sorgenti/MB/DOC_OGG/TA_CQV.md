# CQV - Classe di abilitazione fornitura
 :  : DEC T(ST) K(CQV)
## OBIETTIVO
Controllare le classi di abilitazione alla fornitura di un articolo di una certa CLASSE-FUNZIONALE, riprese dal DATABASE aziendale mediante il programma definito nella tabella di personalizzazione CQ1.
## CONTENUTO DEI CAMPI
 :  : FLD T$LICF **Abilitazione alla classe funzionale**
Campo controllato dalla tabella 'CQQ' (Classi funzionali del prodotto). Indica la classe funzionale massima dell'articolo per cui l'ENTE FORNITORE è abilitato alla fornitura.
 :  : FLD T$LCFF **Abilitazione a classe funzionale per FREE-PASS**
Campo controllato dalla tabella 'CQQ' (Classi funzionali del prodotto). Indica la classe funzionale massima dell'articolo che viene collaudato in FREE-PASS per cui l'ENTE FORNITORE è abilitato alla fornitura. (Un fornitore può essere abilitato alla fornitura di un certo articolo sotto collaudo statistico, ma può non essere abilitato alla fornitura in free-pass dello stesso).
