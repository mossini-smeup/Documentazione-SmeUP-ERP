## CONTENUTO DEI CAMPI

 :  : FLD W5PROG**Progressivo**
Definisce l'identificativo di una registrazione all'interno dell'archivio di transito.
Non obbligatorio che corrisponda all'identificativo che si vuole attribuire alla registrazione definitiva.
Questo capo va riempito nello stesso modo per tutti i record che definiscono una registrazione.

 :  : FLD W5TREC**Tipo Record**
Definisce il contenuto del campo W5REC nel quale viene memorizzato l'intero tracciato record del file di riferimento.
I tipi record gestiti, con l'indicazione del relativo file di riferimento sono : 
- E4 :  Testata          C5TREG0F
- E5 :  Riga             C5RREG0F
- RR :  Rata             C5RATE0F
- MH :  Analitica        C5MOAN0F
- C4 :  Ritenute         C5RITE0F
- DD :  Note di Testata  NTSTRU0F

 :  : FLD W5RIGA**Riga**
Definisce per il tipo record E5 la numerazione della riga all'interno di una registrazione, mentre per i tipi record RR, MH identificano la riga di riferimento.

 :  : FLD W5IDOJ**ID Oggetto**
E' opzionale per il tipo record E4 e se riempito definisce il n° di registrazione verrà attribuito applicando la registrazione.
E' invece obbligatorio per i tipi record RR e MH, per i quali identifica l'identificativo che verrà passato anche ad i record definitivi.

 :  : FLD W5CORD**Criterio di Ordinamento**
Se valorizzato, nel caso di applicazione di massa è possibile applicare le sole registrazioni che presentano in comune la stessa valorizzazione per tale campo.

