[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/NfFqHOKP)
# Uppgift 8 - Skapa en klass för strängkryptering

## 1. <a name='Syfte'></a>Syfte

Syftet med denna uppgift är att få praktisk erfarenhet av att arbeta med
klasser, metoder, undantagshantering, och strängmanipulering i Python genom att
utveckla en enkel krypteringsmekanism.

<!-- vscode-markdown-toc -->

- 1. [Syfte](#Syfte)
- 2. [Förberedelser](#Frberedelser)
- 3. [Uppgiftsbeskrivning](#Uppgiftsbeskrivning)
  - 3.1. [Detaljer](#Detaljer)
    - 3.1.1. [Skapa klassen: SubstitutionCipher](#Skapaklassen:SubstitutionCipher)
    - 3.1.2. [Skapa undantaget: InvalidSubstitutionCipher](#Skapaundantaget:InvalidSubstitutionCipher)
    - 3.1.3. [Tips](#Tips)
    - 3.1.4. [Exempel](#Exempel)
- 4. [Inlämningsinstruktioner](#Inlmningsinstruktioner)
- 5. [Anteckningar](#Anteckningar)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## 2. <a name='Frberedelser'></a>Förberedelser

- Repetera grunderna i Python om klasser, strängar, och undantag.
- Läs om av [substitutionskryptering](https://simple.wikipedia.org/wiki/Substitution_cipher)
  innebär.

## 3. <a name='Uppgiftsbeskrivning'></a>Uppgiftsbeskrivning

Uppgiftens mål är att skapa en klass, `SubstitutionCipher`, som implementerar en
enkel substitutionskryptering. Denna klass ska kunna kryptera och dekryptera
texter genom att ersätta varje bokstav med en annan enligt en fördefinierad
mappning.

### 3.1. <a name='Detaljer'></a>Detaljer

I den här uppgiften så skapar du en klass `SubstitutionCipher` samt ett eget
undantag `InvalidSubstitutionCipher`. Placera båda två i filen `uppgift.py`.

Var noga med att läsa om avgränsningarna vi gör i uppgiften under rubriken
**Anteckningar** innan du går vidare.

#### 3.1.1. <a name='Skapaklassen:SubstitutionCipher'></a>Skapa klassen: SubstitutionCipher

- **Konstruktorsignatur:** `def __init__(self, map: [(str, str)])`
- **Funktion:** Konstruktorn tar emot en sekvens av tupler som argument. Varje
  tupel ska innehålla två strängar med exakt en bokstav vardera. Dessa tupler
  definierar substitutionsmappningen för kryptering/dekryptering. Varje bokstav
  får endast förekomma en gång i hela mappningen.
- **Felhantering:** Konstruktorn ska validera indata och kasta undantag i fem
  specifika situationer. Vänligen läs i dokumentationen för `TypeError` och
  `ValueError` för att avgöra vilket av dessa två undantag som är lämpligast att
  använda i varje situation:
  1. Om ingen sekvens ges som argument.
  2. Om sekvensen innehåller något som inte är en tupel av längd två.
  3. Om något i tuplarna inte är en sträng.
  4. Om någon sträng i tuplarna inte är exakt ett tecken lång.
  5. Om en bokstav förekommer mer än en gång i mappningen så ska undantaget
     `InvalidSubstitutionCipher` kastas. Detta är ett eget undantag som du
     skapar vilket ska vara baserat på den lämpligaste av TypeError och
     ValueError. Beslutet om vilken av dessa som är mest lämplig att ärva från
     bör baseras på en läsning i Python-dokumentationen.

**Metodsignatur:** `def substitute(self, text: str) -> str:`

- **Funktion:** Metoden tar emot en sträng och returnerar den i
  krypterad/dekrypterad form, baserat på klassens mappning. Tecken som inte
  finns med i mappningstabellen finns kvar oförändrade.
- **Felhantering:** Kasta ett lämpligt undantag om argumentet inte är en sträng.
  Vänligen läs i dokumentationen för `TypeError` och `ValueError` för att avgöra
  vilket av dessa två undantag som är mest lämpligt.
- **Returvärde:** Returnera den modifierade texten.

#### 3.1.2. <a name='Skapaundantaget:InvalidSubstitutionCipher'></a>Skapa undantaget: InvalidSubstitutionCipher

Enligt instruktionerna ovan.

#### 3.1.3. <a name='Tips'></a>Tips

För att kontrollera om ett objekt är en sekvens, kan du använda
`collections.abc.Sequence`. Exempel: `isinstance([], collections.abc.Sequence)`.

#### 3.1.4. <a name='Exempel'></a>Exempel

##### Litet

```python
cipher = SubstitutionCipher([('a', 'm'), ('b', 'n')])
encrypted = cipher.substitute('abba')
print(encrypted)  # -> mnnm
decrypted = cipher.substitute(encrypted)
print(decrypted)  # -> abba
```

##### Tom sekvens

```python
cipher = SubstitutionCipher([])
encrypted = cipher.substitute('hello')
print(encrypted)  # -> hello
decrypted = cipher.substitute(encrypted)
print(decrypted)  # -> hello
```

##### Eget undantag vid felet "teckendubletter"

```python
try:
    cipher = SubstitutionCipher([('a', 'm'), ('b', 'n'), ('a', 'o')])
except InvalidSubstitutionCipher as e:
    # Nedanstående rad körs
    print(f"Ogiltig substitution upptäckt: {e}")
```

##### Stort

```python
mapping = list(zip("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"))
cipher = SubstitutionCipher(mapping)
text = "JACK AND JILL WENT UP THE HILL"
encrypted = cipher.substitute(text)
print(encrypted)  # -> WNPX NAQ WVYY JRAG HC GUR UVYY
```

## 4. <a name='Inlmningsinstruktioner'></a>Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. **Använda Github Classroom:**

   - Du har troligen redan accepterat uppgiften via en länk som tillhandahålls
     av utbildaren och gjort en `git clone` av det tilldelade repositoriet då du
     läser denna text. Det är i detta repository du kommer att hitta `README.md`
     med ytterligare instruktioner.

2. **Modifiera `uppgift.py`:**

   - Din lösning på uppgiften ska skrivas i `uppgift.py`. Det finns specifika
     instruktioner i `uppgift.py` om var du ska placera din källkod.

3. **Lämna in med Git:**

   - När du är klar med din uppgift, använd kommandona `git add .`, `git commit`
     följt av `git push` för att skicka in dina ändringar till GitHub.

4. **Automatiska "smoke tests":**

   - Efter att du har pushat din kod kommer automatiska "smoke tests" att köras.
     Dessa tester indikeras med en grön bock om de passerar, eller ett rött
     kryss om de misslyckas. Om du får ett rött kryss, är det viktigt att du
     klickar dig fram i GitHub tills du kan se varför testerna inte passerade.

5. **Feedback och granskning från utbildaren:**

   - Om dina tester passerar med en grön bock, kan du invänta feedback från din
     utbildare. Utbildaren kan antingen sätta "Request Changes" om ytterligare
     förändringar behövs, eller "approve" om uppgiften är godkänd som den är.
     Det är viktigt att du inväntar någon av dessa innan du väljer Merge.
   - Vid "Request Changes" är det viktigt att noggrant granska feedbacken och
     göra de nödvändiga justeringarna baserat på utbildarens anvisningar för att
     säkerställa att din uppgift uppfyller alla krav.
   - Efter att utbildaren har gjort "Approve" på din inlämning, får du göra en
     "Merge" av din "Feedback"-pull request, men inte förrän ett godkännande har
     erhållits.

6. **Initiera diskussioner i "Feedback"-pull requesten:**

   - Som student är du uppmuntrad att aktivt delta i processen genom att
     initiera diskussioner i din "Feedback"-pull request. Detta är en viktig del
     av inlärningsprocessen, där du kan ställa frågor, begära förtydliganden
     eller diskutera lösningar och feedback med din utbildare. Att engagera sig
     i dessa diskussioner ger dig möjlighet att djupare förstå uppgiftens krav
     och förbättra din kod baserat på interaktionen.

## 5. <a name='Anteckningar'></a>Anteckningar

För att underlätta, utgår uppgiften från följande undantag:

- Klassen ska bara klara av symmetriska byten, det vill säga att om `A` ersätts
  med `B`, så gäller även att `B` ersätts med `A` om man anropar `substitute` en
  gång till. Det gör att exempelvis "skifta varje tecken till nästkommande i
  alfabetet" inte är ett substitutionschiffer som klassen kan hantera. Däremot
  så kan den hantera det populära [rot13](https://en.wikipedia.org/wiki/ROT13).
- Det går bra att behandla tecken med stor och liten bokstav som olika. Men om
  du har tid, så är du välkommen att få den att se till exempel `a` och `A` som
  samma tecken och behålla stor eller liten bokstav på varje position i
  strängen.
- För den intresserade är boken _Kodboken_ av Simon Singh en underhållande och
  informativ läsning som täcker det mesta kring koder, schiffer och hemlig
  kommunikation.

---
