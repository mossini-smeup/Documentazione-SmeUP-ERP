# Descrizione

Un componente è un aggregato di moduli e servizi che può avere un cliclo di vita autonomo rispetto all'applicazione.
Esempio di componenti sono : 
* Database
* Compilatore
* Connettori Web

Vengono (o dovrebbero) essere gestiti i seguenti stati di un componente : 
* Attivo
* Disattivo
* Modificato

## Configurazione
Un componente può essere configurato tramite l'impostazione della reference config.
Una configurazione può contenere oggetti multipli che vengono impostati nel contesto
da cui viene costruito il servizio.
Le configurazioni possono pertanto essere accedute dai servizi tramite annotazione @Inject

