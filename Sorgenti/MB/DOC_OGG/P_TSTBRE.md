# DEC - Decodifica

Questa funzione permette di controllare e decodificare gli scenari utilizzatibili da un certo tipo contatto
anche in funzione di una certa modalità.

Campi Input :  £BRETP      Tipo Contatto
             £BREMO (F)  Modalità
             £BRESC (F)  Scenario input

Campi Output :  £BRESK     Scenario Output
              £BREDK     Descrizione Scenario Output

# CAL - Calcolo Riferimenti

Questa funzione permette di determinare alcuni dati di riferimento di un tipo contatto

**RIF - Riferimenti**

Dato un tipo contatto, la sua categoria ed eventualmente uno scenario (che se non viene passato viene calcolato
dal metodo successivo), ritorna i dati (di fatto sono tabelle) di riferimento dei principali dati esterni collegati
al tipo contatto.

Campi Input :  £BRETP      Tipo Contatto
             £BRECA      Categoria
             £BRESC (F)  Scenario

Campi Output :  £BRESC      Scenario (se non passato)
              £BRECP      Cat.Parametri Comuni
              £BRESP      Cat.Parametri Spec.
              £BRECN      Cont.Note Comune
              £BRESN      Cont.Note Specifico
              £BRECL      Calendario Contab.
              £BRESL      Categoria Listini

**SCE - Scenario**

Dato un tipo contatto determina lo scenario di riferimento del momento

Campi Input :  £BRETP      Tipo Contatto
             £BRECA      Categoria
             £BRESC (F)  Scenario

Campi Output :  £BRESC      Scenario

# AUT - Controllo Autorizzazioni

Questa funzione permette di controllare dato un tipo contatto, uno scenario ed un modalità, la validità
della modalità per quello scenario.

Campi Input :  £BRETP      Tipo Contatto
             £BRESC      Scenario
             £BREMO      Modalità

Campi Output :  £BRE35     Indicatore di Errore
              £BREMS     Messaggio
              £BREFI     File Messaggio

# SET - Setup

Questa funzione dato un tipo contatto permette di ritornare il setup di tutti i campi ed estensioni per
gestibili per questo tipo contatto o in alternativa i setup di tutti gli scenari.

**" " - Campi/Estensioni**

Campi Input :  £BRETP      Tipo Contatto

Campi Output :  £BREND     N° Scenari
              £EDT       Tipo campo
              £EDC       Nome campo
              £EDS       Scenografico
              £EDN       Da Nominativo
              £EDZ       Storico
              £EDI       Intestazione
              £EDO       Tipo Oggetto
              £EDL       Lunghezza Campo
              £EDD       N° Decimali
              £EDA       Autorizzazioni
              £EDV       Attributo visualiz.
              £EDB       Obbligatorio

**SCE - Scenario**

Campi Input :  £BRETP      Tipo Contatto

Campi Output :  £BRENS     N° Scenari
              £BRESS     Sottosettore scenari
              £ESK       Cod. scenari
              £ESD       Descrizione scenari
              £ESL       Definizione scenari
              £ESA       Autorizzazione su scenari
              £ESS       Stringa Autorizzazioni

# FLD - Funzioni su campi

Questa funzione gestisce una serie di elaborazioni a livello di singolo campo.

**RTV - Riempe Valore da record**

Con questo metodo dati in input un record ed il nome di un campo viene ritornato il valore
di tale campo in quel record.

Campi Input :  £BRERE      Record anagrafico
             £BREFC      Nome campo

Campi Output :  £BREFE     Valore Campo Alfanumerico
              £BREFN     Valore Campo Numerico

**VTR - Riempie Record da valore**

Con questo metodo dati in input un record, il nome di un campo ed un valore, viene ritornato
il record con il campo aggiornato con il valore passato.

Campi Input :  £BRERE      Record anagrafico
             £BREFC      Nome campo
             £BREFE      Valore Campo Alfanumerico
             £BREFN      Valore Campo Numerico

Campi Output :  £BRERE     Record anagrafico (aggiornato)

# GES/CON/DEL - Funzioni su riferimenti Esterni

Queste funzioni permettono di gestire i dati esterni legati all'anagrafica. La tipologia di riferimento
esterno viene identificata dal metodo.

Funzioni : 
**GES : **permette richiamare in gestione il dato esterno.
**CON : **in caso di inserimento permette di confermare il dato
**RIE : **permette di cancellare il riferimento esterno

Metodi
**ALL : **    Gestione Parametri/Note di Comuni/Scenario (*)
**SCE : **    Dati Scenario (Parametri e note) (*)
**PAR_SCE : **Gestione Parametri Scenario
**PAR_COM : **Gestione Parametri Comuni
**NOT_COM : **Gestione Note Comuni
**NOT_SCE : **Gestione Note Scenario
**DIC_INT : **Gestione Dichiarazioni di intento (-)
**GES_CAL : **Gestione Calendario (-)


(*) Metodi non validi per funzione GES
(-) Metodi non validi per funzione CON

Campi Input :  £BRETP      Tipo Contatto
             £BRECD      Codice Contatto
             £BRESC (F)  Scenario
             £BREMO      Modalità

