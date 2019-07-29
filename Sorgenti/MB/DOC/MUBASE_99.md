# Guida allo sviluppo

## Generali
* Riutilizza ove possibile il software che scriviamo
* Scomponi i problemi
* Scrivi sempre sistemi di test
* Rilascia di continuo il codice
* Quando il codice e' open source aggiungi intestazione e licenza

## As.UP

* Rispetta il modello OMAC
** O = Object
** M = Manager
** A = API
** C = Command
* Concentra negli oggetti le proprieta' applicative
* Concentra nei manager le logiche applicative
* Nella segnatura metodi prediligi QContextProvider a QContext
* Evita di utilizzare System.out, usa il JobLog
* Ricorda che As.UP e' un server, ogni riavvio corrisponde a un IPL
* Esporta i comandi da OS/400 tramite profilo ASUP in ambiente inglese
* Mantieni i comandi in ordine alfabetico in ASUP/commands.xmi
* Utilizza quando sei certo le annotazioni @Supported, @Todo, @Unsupported, ..
* All'interno di API, solleva dove possibile eccezioni applicative (OperatingSystemMessageException -> CPFxxxx)
* Non toccare il codice generato automaticamente (QDataStruct, QEnum, etc..)
* Utilizza dove possibile gli switch sugli enumeratori
* Utilizza quando disponibili librerie del framework Eclipse

## Nomenclatura delle classi
* Le classi di utility con metodi static devono avere il postfisso 'Helper' (XMLCommandHelper, DatabaseHelper)
* I servizi di utility devono avere il postfisso 's' e il nome dell'oggetto interessato (QStrings, QURIs, QFiles, QStreams, etc..)

## Nomenclatura API personalizzate
* QASxx As.UP
* QMUxx Sme.up

## Sme.UP
* Utilizza ove possibile servizi e /COPY
* Documenta in SCP_DOC quanto sviluppato
* Esponi tramite Looc.UP quanto sviluppato

## Eclipse EMF
* Modella quanti piu' oggetti 'applicativi' possibile
* Poni attenzione alla proprieta' 'containment' nella definizione di relazioni, generalmente deve essere impostata a 'true'
* Le proprietà multiple devono avere nome al plurale (es. scheduledDays)
* Limita codice specifico nel generato EMF (.genmodel)
* Delega a Manager
* Segnala quando indispensabile con @Generated NOT
* Attenzione agli oggetti JavaXXXX dei modelli .ecore, generalmente non sono serializzabili
* Evita l'utilizzo di oggetti JavaMap/EMap


## JAVA
* Porre attenzione alle funzioni trim() su string, generalmente da evitare
* Non utilizzare 'default' nei costrutti 'case'
* Prediligi le RuntimeException
* Limita la conservazione dei dati in oggetti String, dove sensato prediligi Stream o API Sme.UP (-> £JAX) (*)
* Per la gestione eventi/listener prediligi la forma Enum<EventType>, manager.fireEvent(event), listener.handleEvent(event)

## Eclipse IDE
* Utilizza il formattatore di codice standard (importare dal progetto mu.product)
* Evita segnalazioni di warning nei progetti
* Attiva warning per resource leak
