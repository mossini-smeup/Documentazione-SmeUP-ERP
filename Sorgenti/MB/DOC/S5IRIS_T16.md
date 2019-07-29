
#  PROCEDURA ALLINEAMENTO PROGRAMMI SCHEDULATORE TRA SMEDEV

L'Obiettivo di questo documento è spiegare le attività necessarie ad allinare i programmi necessari alla schedulazione qualora non  sia possibile installare un'aggiornamento completo di Sme.up(di versione o di smedev). Se non siete in questo caso ignorate il presente documento.


Quando si installa una nuova versione della BCD occorre eseguire le seguenti azioni

##  /copy

Copiare dalla QILEGEN di SMEDEV  le seguenti /COPY
   - £S5SMDS
   - £S5SMPLI
   - £S5SMPLO
   - £BCDDS1

##  Programmi

* Copiare tutto il file BCDSRC dalla SMEDEV e ricompilare i programmi
* Controllare il livello di aggiornamento dei programmi B£BCD* rispetto all'ultima versione presente in SMESRC/SMEDEV, e  l'eventuale presenza di nuovi programmi con questa radice.
Questi programmi riportano in testa la riga di modifica, ma non vengono emesse NEWS.

* Controllare il livello di aggiornamento dei programmi JAJAT0PS e B£TRA_01 presenti nel file JASRC

## Allineamento Tabelle
Controllare il livello di aggiornamento delle seguenti tabelle : 
   - B§G
   - BRM
   - S5B
   - S5X (NB :  è un settore 'L' di sola definizione che guida la £G30)

## Documentazione
Ricordo che la documentazione dello script BCD è il membro B£BCDO in SMEDEV/DOC.

## Script Schede
li script della scheda della schedulazione sono i seguenti membri (in SMEDEV/SCP_SCH - S5BASExx

## Indici Schedulazione
Per l'intestazione degli indici dinamici occorre il programma D5CO_12. Riferirsi all'help della tabella S5B per la loro memorizzazione in D5COSO. Per creare le tabelle degli indici utlizzare la funzione di creazione D5FS01A (Funzione / metodo / Contesto  :  Gestione / Completa / S5)

## Voci
opiare da SMEDEV/DOC_VOC il membreo S5IRIS che contiene le voci degli errori. Inserire l'oggeto VOCE (VO) in tabella *CNTT

## Script Schedulazione
Allineare Script PAR_SCP di SMEDEV con quello contenuto nella B§G del motore di schedulazione.



