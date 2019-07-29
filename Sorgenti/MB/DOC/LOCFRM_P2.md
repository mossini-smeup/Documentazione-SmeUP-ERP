# Versione 6.1 del 21 Aprile 2006
Aggiunta al file di configurazione la parte di setup della stampa a Runtime (quella che appare nella finestra) per avere a disposizione un default.
Gestite le variabili di loocup nel file di setup :  gli attributi del XML possono contenere variabili che vengono risolte prima della creazione del PDF.
Gestite le precedenze sulla configurazione di stampa :  prima la configurazione nel XML che arriva da AS, poi alternativamente quella nel file di setup.

## Doc Generator subv. 2.8 - Modifica 21 Gennaio 2006
Aggiunta specifica NPG per indurre salto pagina nel testo della documentazione

# Versione 6.0 del 10 Aprile 2006
Gestione setup del PDF da file di configurazione.
 T(Le caratteristiche gestite nel setup sono le seguenti : )
- tipi di font (nome, colore, stile, dimensione)
- tipi di testo (tipo di font collegato e interlinea)
- tipi di paragrafo (tipo di testo collegato, tipo di paragrafo {testo, lista, tabella}, allineamento, indentazione)
- titolo del documento (testo, presenza delle informazioni sul file)


# Versione 5.2 del 26 Gennaio 2006
## Doc Generator subv. 2.7 - Modifica 30 Gennaio 2006
Sistemata l'inclusione dei file attaverso la specifica _B_DEC per i problemi che c'erano con la successione delle specifiche nel documento PDF
## Sch Generator subv. 2.4 - Modifica 26 Gennaio 2006

- Ristrutturato parser documento XML che ora si basa sul Layout.
- Gestione del parametro **TitSez** nelle specifiche _B_G.SEZ**per poter passare il titolo alla sezione (sembra però che il JATRE adibito alla costruzione del XML non lo passi a Loocup)
## Sch Generator subv. 2.4 - Modifica 1 Febbraio 2006

- Gestito valore ***NONE** nei titoli delle sottosezioni per non dare il titolo.
- Gestito scaling delle immagini nelle specifiche _B_D.IMG.OGG :  se l'immagine ha dimensioni maggiori del foglio la restringe a quelle del foglio, altrimenti mantiene le dimensioni dell'immagine senza stretcharla.
