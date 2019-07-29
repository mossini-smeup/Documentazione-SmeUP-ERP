## Passi sequenziali per impostazione snella di base

- Inserire tabella M5B, elemento ** (scenario di base)	
-  definire in M5F le fonti pianificate di acquisto, produzione e Conto lavoro, APN OPN e CPN
- FASARE M5**P E COLLEGARE I PROGRAMMI DI RILASCIO OPPORTUNI A APN E OPN
- Definire in M5F le fonti pianificate di impegno produzione e C/lavoro IPN e ILP
- Definire nelle politiche M5A le due politiche fondamentali per acquisti e produzione, A01 e P01
- Definire la fonte PPR punto di riordino in M5E
- Impostare tabella M51 :  le politiche fondamentali di produzione ed acquisto A01 e p01 che pianificano rispettivamente APN e OPN/IPN
- Impostare tabella M51 :  il ricalcolo livello minimo è consigliato.
- Impostare calendario risorsa CDL **
- Impostare tabella MAG con magazzino fondamentale dove è riportata CDL **
- Definire almeno la fonte fabbisogno principale negativa, OCA in M5F
- Definire almeno una fonte di giacenza esistente, meglio se tutte le aree di disponibilità in tab M5E, Gxx
- Definire il gruppo fonti MRP, che comprende le fonti Gxx, APN, OPN, CPN, IPN, ILP, OCA


## Passi ulteriori per impostazione piu' potente

- Inserire fonti di eccedenza QEE e QEF in M5E e M5F
- Definire scorta minima SC in M5E
- Definire politica C01 in M5A per conto lavoro, che pianifica CPN/ILP
- Impostare Fonti M5F di Acquisto, Produzione e C/lav. ACQ, PRO, ACL
- Impostare fonti M5F di impegno rilasciato IPR e ICL
- Fasare tabella C£G, elemento AR_MT per impostazione risalita parametri di pianificazione
- Aggiornare M51 con QEE, QEF, PPR e Gruppo fonti MRP con altre
- Definire politiche e parametri di pianificazione opportuni

