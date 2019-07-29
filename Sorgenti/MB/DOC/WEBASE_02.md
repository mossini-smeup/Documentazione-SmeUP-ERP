# Architettura
Web.UP si basa sugli stessi concetti di Looc.UP.
In particolare **le pagine web vengono generate a partire dagli script di scheda**

![WEBASE_036](http://localhost:3000/immagini/WEBASE_02/WEBASE_036.png)
**1. Si basa sugli script di scheda**
 :  : DEC T(OG) P() K(MBSCP_SCH)
**2. Si basa sui servizi**
 :  : DEC T(OG) P() K(V3ASE)
**3. Si basa sui componenti grafici (J1 GRA)**
 :  : DEC T(OG) P() K(J1GRA)
**4. Comunica con il server applicativo tramite FUN**
 :  : DEC T(OG) P() K(J1FUN)

## Nota importante
_7_Web.UP non supporta l'Emulazione 5250

![WEBASE_038](http://localhost:3000/immagini/WEBASE_02/WEBASE_038.png)
# Componenti

I componenti di Web.UP sono gli stessi di Looc.UP, tuttavia, per motivi di sviluppo e per le differenti tecnologie, ci sono delle differenze : 
- non tutti i componenti sono portati in web. Ad esempio :  Emulatore, Device, Workflow designer
- alcuni componenti esistono silo in web. Ad esempio :  Calendario
- i comportamenti sono leggermente diversi e si adattano al device
- non tutte le funzionalità sono replicate, perchè deprecate, perchè impossibili da replicare o perchè inadeguate

Una demo completa dei componenti è disponibile nello **Showcase di Web.UP**
[http://webuptest.smeup.com/](http://webuptest.smeup.com/)

### Tutti i componenti e le funzionalità sviluppate sono presenti nello Showcase
### Ciò che non è presente nello Showcase non è stato sviluppato
### Le funzionalità in sviluppo e non utilizzabili in produzione non contrassegnate come tali






