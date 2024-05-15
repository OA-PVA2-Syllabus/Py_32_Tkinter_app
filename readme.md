# PVA2 - Programování a vývoj aplikací
## Cvičení 32: GUI Tkinter App

Dokumentace Tk: `https://tk-tutorial.readthedocs.io/en/latest/intro/intro.html`

### 1 Binding
`https://tk-tutorial.readthedocs.io/en/latest/event/event.html?highlight=bind`
Zdrojový kód upravujte v souboru `binding.py`

Přimějte `button1` spustit funkci `increase_value` BEZ použití parametru `command=`

V předchozích lekcích jste vytvořili funkční tlačítka, ale co když chceme mít klávesové zkratky nebo něco provést pravým tlačítkem myši?

Vázané akce spojují funkci s událostí/vstupem, který se odehrává v okně.

1. Proměnná čítač uchovává aktuální hodnotu proměnné čítač.
2. Funkce increase_value zvyšuje hodnotu proměnné.
3. Poté funkce aktualizuje popisek label1.
4. Před otevřením okna navážeme funkci na tlačítko. Takže když tlačítko obdrží vstupní událost <Button-1>, spustí se funkce increase_value.

Seznam běžně používaných [vstupních událostí](vstupni_udalosti.md) budete ho potřebovat.

### 2
* Deklarujte funkci decrease_value, která bude po pravém kliknutí myši zmenšovat hodnotu o 1.
* Za využití metody `config` zařiďte, aby před aktualizací snížil text popisku `label1` o 1.

### 3
Deklarujte nový program `mys.py`, který zobrazí zobrazí zprávu ve widgetu popisku.
* Pokud do okna vstoupíte myší, zobrazí se ve widgetu Label zpráva "Hello.".
* Pokud myš opustí okno, zobrazte ve widgetu Label zprávu "Goodbye.".

### 4 Pozadi
* Vytvořte program `pozadi.py`, který změní pozadí, pokud kliknete levým tlačítkem myši,
a zobrazí předchozí barvu, pokud kliknete pravým tlačítkem myši.
* Barva pozadí se taktéž bude měnit pomocí levé a pravé šipky.

`window.config(bg=)`

### 5 Kámen, nůžky, papír
Vytvořte jednoduchou hru kámen, nůžky, papír.

* Uživatel musí mít možnost vybrat si kámen, nůžky nebo papír.
* Váš program musí náhodně vybrat kámen, nůžky nebo papír.
* Váš program musí vést průběžné skóre pro lidského a počítačového hráče.
* Program musí vypisovat následující údaje:
  * Volba hráče
  * Volba soupeře (počítače)
  * Aktuální skóre hráčů
  * Aktuální skóre soupeře
 
Nápověda: Zahrňte alespoň jeden z následujících widgetů:
* Button
* Label
