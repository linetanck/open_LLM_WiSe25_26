# Open LLMs in der Praxis: Liebeslieder
Projekt für das Seminar Open LLMs in der Praxis.

Karoline Tanck 7449219

## Aufgabenstellung
In diesem Projekt sollen open LLMs auf ihre Fähigkeit Texte zu interpretieren, getestet werden. Dabei wird sich fokussiert auf Songtexte eines bestimmten Artist (tbd.) und auf einen Bestimmten Aspekt: die Einstellung von dem lyrischen Ich zu dem lyrischen Du. Es soll um die Art des Liebesliedes gehen.

Dabei bekommt das Modell folgende Promts
```
'You are a Person with a high school degree and have no previous knowledge of this musical artist. Using the lyrics of each song, please sort it in one of these categories: '
```
Die Kategorien stehen noch nicht endgültig fest, orientieren sich aber an: 
* "happily together", 
* "broken up", 
* "longing", 
* "not a love song"

Grundsätzlich lassen sich Ergebnisse dieses Projektes auch auf andere Formen von Lyrik übertragen, zum Beispiel Gedichte. Sollten das genutzte offene LLM gut performen in diesem Projekt, dann ermöglichen LLMs das schnelle Analysieren solcher kurzen künstlerischen Texte.
## Daten:
Bei der Auswahl eines Datensatzes wird darauf geachtet, dass genug Lieder eines Artist im Datensatz sind. Zusätzlich aufgrund der Notwendigkeit einer manuellen EInteilung der Songs in die Kategorien ist es auch wichtig, dass alle Lieder gerne einmal gehört werden. 

https://www.kaggle.com/datasets/mllion/one-direction-all-songs-with-lyrics/data
https://github.com/adashofdata/taylor_swift_data/blob/main/Taylor_Swift_Words_Data.xlsx

## Modell
Für die Bearbeitung des Projekts wurden erste Experimente mit dem Modell [llama3.2:3b](https://ollama.com/library/llama3.2:3b) via Ollama gemacht. In der Entscheidungsfindung welches Modell genutzt wird, wurde neben der Offenheit hauptsächlich auf die Größe des Modells in Relation zur Leistungsfähigkeit geachtet. Das Projekt soll auf einem Laptop mit 8GB Arbeitsspeicher laufen, da dies auch ein zukünftiges Anwendungsszenario sein könnte. Laut Ollama übertrifft llama3.2:3b viele der anderen offenen Modelle und ist besonders gut darin, Zusammenfassungen zu erstellen.

## Projektverlauf
### Erste Tests
In der Datei **erste_Versuche.py** sind erste Bemühungen mit llama3.2:3b dokumentiert, sowie der setup Prozess von Ollama.  
Erste Versuche wurden nur mit dem Text des Songs "You Belong With Me" von Taylor Swift gemacht.
### Ausstehende Aufgaben  
- Datensatz festlegen
- Datensatz richtig formattieren
- Datensatz manuell einordnen
- Einen Song testen
- Output des Modells ins richtige Format
- Code zum Vergleich zwischen LLM output und Ziel Kategorie
