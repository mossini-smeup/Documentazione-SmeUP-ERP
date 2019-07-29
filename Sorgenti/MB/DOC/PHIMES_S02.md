## VERIFICHE E AZIONI PRELIMINARI
Prerequisito per installare il pacchetto MES di SmeUP è la presenza almeno di una versione V5R1.
Per installare il prodotto MES è stato preparato un pacchetto SDST_PH004 scaricabile dall'area riservata.

_2_Video
 :  : DEC T(J1) P(URL) [https://www.youtube.com/watch?v=1Qvm1qAGuDc&list=PLzGRFHu9NZOO0tErEHV1WtakGOTy7alz9&index=2&t=0s+
](https://www.youtube.com/watch?v=1Qvm1qAGuDc&list=PLzGRFHu9NZOO0tErEHV1WtakGOTy7alz9&index=2&t=0s+
)
) D(Scarico pacchetto MES)
 :  : DEC T(J1) P(URL) [https://www.youtube.com/watch?v=XjVEpkmygNA&list=PLzGRFHu9NZOO0tErEHV1WtakGOTy7alz9&index=3&t=0s+
](https://www.youtube.com/watch?v=XjVEpkmygNA&list=PLzGRFHu9NZOO0tErEHV1WtakGOTy7alz9&index=3&t=0s+
)
) D(Installazione pacchetto)




_2_PASSI INSTALLAZIONE
- Creazione anagrafiche macchine (obbligatorio usare il tipo risorsa "MAC")
- E' mandatorio indicare nell'anagrafica di ogni macchina (BRRISO) il magazzino di riferimento, perchè necessario all'elaborazione corretta della £PHI per gli avanzamenti.
- Eseguire PHUTX01 per allineare le definizioni
- Eseguire pgm PHUT02 per creare gli elementi di tabella standard e i sottosettori mancanti (la routine allinea tutti gli elementi non presenti e crea i sottosettori)
- Aprire LoocUp - creare una nuova lista RIMAC (LI RIMAC)
- Lanciare UPP dallo spotlight richiamare la PH_038 con la lentina.
- Creare un SCP_CLO A_AMBENTE in cui replico la chiamata PH_038 ad esempio
- Definire sulla singola macchina l'accesso come PH_049
- Verifica P5K (e relative P5E,P5D e P5F£R)
- Controllo P5C collegate a P5K per dichiarazioni P5ATTI
- Definizione P56 con riferimento a eventi P5K base e Ordine FERMO gestionale
- Controllare gli elementi della P5B per le sottocausali per tipologia di fermo specifiche dell'azienda
- Configurazione LOA37 in SCP_SET e relativo programma LOA37_PX per lettura eventi
- Verificare presenza Oav oggetto E3£RI. E' importante che sia lanciato specificando il parametro perchè verranno creati degli oav specifici solo per il tipo £RI.
- Verifica impostazione turni macchine con B§R (codice turno) e con OLG allineati (rilancio fasatura calendari con funzione a menù)
- Installazione  Provider specifico per LOA37/macchine
- Installazione WebUp + Provider specifico per web
- Creazione utente generico ad esempio POSMES pwd POSMES01 per accesso diretto con SCP_CLO  per pannello operativo di una postazione specifica.
-- att. il cod. utente serve solo per permettere l'accesso DIRECT alla postazione, gli operatori che lavoreranno sulla macchina si identificheranno tramite il loro cod. operatore/cod. dipendente

_2_Configurazione connessione con le macchine e interfaccia MACCHINE-SMEUP
* Configurazione di un server Windows con Smeup Provider versione V5R1 per comunicazione con SmeUP ERP
* Istallazione e configurazione software Kepware con relativo plugin IOT Gateway (https://www.kepware.com/en-us/products/kepserverex/advanced-plug-ins/iot-gateway/documents/iot-gateway-manual.pdf)
* Configurazione connettori con le macchine (in base alla tipologia del collegamento previsto (OPC DA/OPC UA/PLC/MODBUS) deve essere configurato il connettore specifico del KEPWARE.
** KEPWARE permette di definire un' interfaccia generica di accesso a diverse tipologie di macchine e protocolli)
* Creazione script A37 di variabili macchine lato SMEUP. La suddivisione dello script viene fatto in base al reparto/tipologie di macchina/linee o altro e viene stabilito/condiviso in fase di configurazione durante le prime riunioni con il personale IIOT di SmeUP
** Tutti i dati in INPUT/OUTPUT vengono gestiti tramite elenchi di variabili/TAG definiti nel LOA37_XY creato a partire dal LOA37_£H di esempio. E' possibile interagire con queste variabili sia in modalità push che pull e sia in lettura che scrittura.
** In SmeUP tutte le variabili del campo (riferite anche con il termine TAG) sono gestite tramite questo framework chiamato in modo semplice A37. Questo modo generalizza la modalità con cui SmeUp gestisce macchinari di tipologie differenti
** Ogni macchina può restituire in OUTPUT segnali segnali on/off, pezzi fatti, pezzi scartati, eventuale moltiplicatore oltre a dati di processo quali temperature, velocità media, dati di pressione o altro.
** Inoltre ogni macchina potrebbe avere a disposizione tag in INPUT a cui passare informazioni quali il cod. di attrezzatura attualmente in uso, articolo/part-program , ordine di produzione, ciclo standard previsto (info utili in caso di certificazione Industry 4.0). Queste informazioni passate al PLC o alla macchina normalmente sono poi visualizzate sul pannello operatore.
* In questa una fase iniziale è importante identificare quali sono i valori che devono essere recepiti e quali possono essere scritti sulla macchina (la possibilità di scrivere dati sulla macchina dipende dalle possibilità date dal fornitore in fase di installazione o quelle che possono essere poi modificate durante la configurazione con SmeUP ERP)
* Una volta definite le variabili che arrivano dalla macchina queste devono essere configurate sul parametro £MA associato alla macchina.

_2_UTILIZZO £PHI
- [Eventi&-x2f;Attività MES](Sorgenti/MB/DOC/PHIMES_S04)



_2_TABELLE UTILIZZATE-MODIFICABILI
Le seguenti tabelle devono essere allineate/modificate a seconda delle proprie esigenze.
 :  : DEC T(ST) K(P5C)
 :  : DEC T(ST) K(P5F£R)
 :  : DEC T(ST) K(P56)
 :  : DEC T(ST) K(P5D)
 :  : DEC T(ST) K(P5K)

_2_OAV NECESSARI
 :  : DEC T(OA) P(RIMAC) K(J/F01)
 :  : DEC T(OA) P(RIMAC) K(J/F02)
 :  : DEC T(OA) P(RIMAC) K(J/F03)
 :  : DEC T(OA) P(RIMAC) K(J/G01)
 :  : DEC T(OA) P(RIMAC) K(J/G02)
 :  : DEC T(OA) P(RIMAC) K(J/P01)
 :  : DEC T(OA) P(RIMAC) K(J/P02)
 :  : DEC T(OA) P(RIMAC) K(J/P03)
 :  : DEC T(OA) P(RIMAC) K(J/P04)
 :  : DEC T(OA) P(RIMAC) K(J/P05)
 :  : DEC T(OA) P(RIMAC) K(J/P06)
 :  : DEC T(OA) P(RIMAC) K(J/P07)
 :  : DEC T(OA) P(RIMAC) K(J/P08)
 :  : DEC T(OA) P(RIMAC) K(J/P09)
 :  : DEC T(OA) P(RIMAC) K(J/P10)
 :  : DEC T(OA) P(RIMAC) K(J/P11)
 :  : DEC T(OA) P(RIMAC) K(J/P12)
 :  : DEC T(OA) P(RIMAC) K(J/P13)
 :  : DEC T(OA) P(RIMAC) K(J/P14)
 :  : DEC T(OA) P(RIMAC) K(J/P15)
 :  : DEC T(OA) P(RIMAC) K(J/P16)
 :  : DEC T(OA) P(RIMAC) K(J/P17)
 :  : DEC T(OA) P(RIMAC) K(J/P18)
 :  : DEC T(OA) P(RIMAC) K(J/P19)
 :  : DEC T(OA) P(RIMAC) K(J/P20)
 :  : DEC T(OA) P(RIMAC) K(J/P21)
 :  : DEC T(OA) P(RIMAC) K(J/P22)
 :  : DEC T(OA) P(RIMAC) K(J/P23)
 :  : DEC T(OA) P(RIMAC) K(J/P24)
 :  : DEC T(OA) P(RIMAC) K(J/P25)
 :  : DEC T(OA) P(RIMAC) K(J/P26)

_2_PARAMETRI
Parametri Macchina
La categoria £MA contiene tutti i parametri che vengono usati nel MES.
 :  : DEC T(TA) P(C£E) K(£MA)

Tra i vari parametri possibili ci sono quelli che definiscono come veicolare i dati ricevuti dal LOA37, se una macchina è gestita manuale o se è collegata con dei dispositivi, l'elenco delle causali di fermo ammissibili per quella macchina, l'elenco delle causali di scarto.
 :  : DEC T(TA) P(B£N£H)  K(M50)
 :  : DEC T(TA) P(B£N£H)  K(M60)
 :  : DEC T(TA) P(B£N£H)  K(M62)
 :  : DEC T(TA) P(B£N£H)  K(M65)
 :  : DEC T(TA) P(B£N£H)  K(M70)
 :  : DEC T(TA) P(B£N£H)  K(M71)
 :  : DEC T(TA) P(B£N£H)  K(M74)
 :  : DEC T(TA) P(B£N£H)  K(M78)
