# FUNZIONI e METODI

## INZ.LOT Inizializza Lotto
 Prepara un nuovo lotto (Obbligatorio).

## INZ.SLT Inizializza Sottolotto o Transazione
 Prepara un nuovo sottolotto.
 Il sottolotto è il legame con cui si tengono insieme i vari oggetti applicativi e serve a parità  di lotto, a separare la collezione di tipi record
 Ogni sottolotto può avere un solo oggetto di tipo DO.

## WRI Scrittura
 Aggiunta di un nuovo record al sottolotto istanziato
 Sono stati implementati i seguenti tracciati (con il relatovo tipo record)
 V5TDOC - Testate documento (DO)
 V5RDOC - Righe   documento (DR)
 C£CONR - Parametri (C£)
 NTSTRU - Note strutturate (NT)

## APP.LOT Applicazione Lotto
 Applicazione del lotto. Per ogni sottolotto, valutando coerenza e integrità delle informazioni,  in assenza di errore istanzia i records negli appositi files.

## VER.STR Verifica struttura
 Deve esistere almeno l'oggetto DO

## VER.OGG Verifica oggetti
 Non ci devono essere oggetti assenti nel sistema informativo, questa verifica viene eseguita  utilizzando la /copy £V7x.

# COMPORTAMENTO APPLICATIVO
Durante la verifica si utilizza il flag 1 per indicare che il sottolotto è in errore per poterlo escludere dall'applicazione.
L'applicazione esegue in automatico una verifica di struttura e di oggetti, una volta applicato  il sottolotto viene annullato.
