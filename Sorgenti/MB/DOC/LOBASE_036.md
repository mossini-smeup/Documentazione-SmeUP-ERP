## Elementi XML presenti e gestiti nel file scambiato (Root element= UIDoc)
### Elemento "Keys"
Contiene in sottoelementi K1, K2, K3 le chiavi di riferimento del documento. Ogni chiave contiene gli attributi Tipo, Parametro, Codice e Testo
### Limiti
- Non gestisce ancora la risalita sui tipi **
### Esempio
 :  : I.XML
<Key>
<K1 Tipo="ST" Parametro="" Codice="V5D" Testo="TIPI DOCUMENTO" Obl="1" StarStar="0"/>
<K2 Tipo="" Parametro="" Codice="" Testo="" Obl="2" StarStar="1"/>
<K3 Tipo="" Parametro="" Codice="" Testo="" Obl="3" StarStar="0"/>
</Key>
 :  : I.XML.END
## Elemento "Setup"
Contiene, nell'elemento Program, l'elemento EDT con le informazioni sul testo che si sta trattando. Gli attributi gestiti in EDT sono Tipo (valori possibili HTML, TXT, RUL e RPG) che indica il tipo di testo trattato, NoMod (valore possibile 1) che indica che il tipo di documento è fissato, Control cui viene associato il configuratore nel caso di testo controllato.
### Limiti
- Non presenta syntax highlight nel testo sintatticamente sensibile
### Esempio
 :  : I.XML
<Setup>
  <Program>
    <EDT Tipo="HTML" NoMod="1" Control=""/>
  </Program>
</Setup>
 :  : I.XML.END
## Elemento "Buttons"
Gestisce, attraverso la presenza di elementi Button (da 1 a 3), delle funzioni di Salva, Salva con Nome e Elimina I tre elementi Button possiedono due attributi Name (Nome del bottone) e Status (1= attivo, 0= disattivo)
### Esempio
 :  : I.XML
<Buttons>
<Button Name="Salva con nome" Status="1"/>
<Button Name="Salva" Status="1"/>
<Button Name="Cancella" Status="1"/>
</Buttons>
 :  : I.XML.END
## Elemento "Contenuto"
Contiene, in un'unica struttura CDATA il testo gestito
### Esempio
 :  : I.XML
<Contenuto>
Inserire elemento CDATA (qui parentesi separate per non farlo riconoscere all'interprete)
< ! [ CDATA [ Testo libero multiriga ] ] >
</Contenuto>
 :  : I.XML.END
