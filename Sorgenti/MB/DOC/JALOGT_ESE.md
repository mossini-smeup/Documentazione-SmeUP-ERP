# VARI ESEMPI DI LOG
 :  : INT Premesse
Per ognuno di questi esempi è necessario abilitare il log(JA1)
 :  : FIN
# Abilitare il log di loocup
Set. JAL Funzioni Client/Server Log
Ele. DATSES
Descrizione          Log loocup
Tipologia messaggio  C                  Collegamento
Time out Secondi        60
Modalita Log Rid/Com C                  Completo
Modalita coll        L                  LoocUp
Agg collegamento     1                  SI
 :  : INT Caratteristiche
Se una sessione viene chiusa im modo anomalo il log dichiara chiusa la
Sessione 60 sec dopo l'ultima operazione effettuata
 :  : FIN
# Abilitare il log di webup

Set. JAL Funzioni Client/Server Log
Ele. DATUSR
Descrizione          Log webup Collegamento
Tipologia messaggio  C                  Collegamento
Time out Secondi        60
Modalita Log Rid/Com C                  Completo
Modalita coll        W                  WebUp
Agg collegamento     1                  SI

Set. JAL Funzioni Client/Server Log
Ele. LISHTM
Descrizione          Lis htm
Tipologia messaggio
Time out Secondi
Modalita Log Rid/Com C                  Completo
Modalita coll        W                  WebUp
Agg collegamento     1                  SI

Set. JAL Funzioni Client/Server Log
Ele. LISOGG
Descrizione          Lisogg
Tipologia messaggio
Time out Secondi
Modalita Log Rid/Com C                  Completo
Modalita coll        W                  WebUp
Agg collegamento     1                  SI

 :  : INT Caratteristiche
lo scollegamento avviene 60 sec dopo l'ultima operazione effettuata
Le operazioni considerate sono : LISOGG e LISHTM
Che vengono a loro volta tracciate in webup
