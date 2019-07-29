# B§1 - Gestione ambienti per utente
 :  : DEC T(ST) K(B§1)
## OBIETTIVI

Qui vengono elencati gli ambienti ammessi per utente.

### CONFIGURAZIONE DELLE AZIONI UTENTE

- L'elenco delle azioni di un utente dipende dal gruppo azioni previsto per l'utente. Il
  default è**"**"**, ma tramite l'elemento della B§1 intestato all'utente (coincidente con l'elemento
  della B§1 dato da**"**"+ profilo utente**) posso andare a differenziarlo.

- Identificato il gruppo le azioni utente vengono identificate dagli elementi della B§1
  con codice**"$$"+ codice gruppo azioni**.

## CONTENUTO DEI CAMPI
 :  : FLD T$B§1A **Tipo accesso**
- _7_S :  Menù SMEUP
- _7_P :  Menù SMEUP :  Richiamo con Parametri
- _7_A :  Menù ACG
- _7_C :  Stringa comando
- _7_J :  Azione Java
 :  : FLD T$B§1O **Salta in Loocup**
Se impostato, non mostra in loocup l'ambiente a cui l'elemento di tabella si riferisce.
 :  : FLD T$B§1P **Ambiente NON Sme.up**
Se impostato, indica che l'mabiente non è Sme.up, ossia non ha in linea librerie dati e programmi Sme.up.
I tipi accesso S, P e G non sono compatibili con il valore 1 per questo flag.
Tale campo non è significativo nel caso di tipo accesso A (ACG) in quanto in quel caso è
sicuramente non sme.up
