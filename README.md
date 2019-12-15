# GKLB_INTM020-Mikroelektromechanikai rendszerek tárgy vizsgafeladata
## Passzív infra mozgásérzékőlős, tömegmérésen alapuló automata tápadagoló

### 1. Projekt kiválasztása

Vizsgafeladatnak egy testtömeg alapján működő automata száraztáp adagoló berendezés modelljét választottam. Az alapgondolat onnét eredt, hogy családon belül problémát szokott okozni, hogy éppen ki eteti a macskát, miért üres a tányérja, túl sok táp lett kiadagolva, stb. Az adagoló hasonlóan működne gyermekeim forgó lapátkereskes műzli adagoló berendezéséhez. (lsd. 1. kép)![Műzliadagoló](https://github.com/vassb76/RSLRCV_MEMS/blob/master/M%C5%B1zliadagol%C3%B3.png "1. kép Műzliadagoló")

### 2. Hardver és szoftverkörnyezet, szenzorok, motor kiválasztása

A projekt kivitelezéséhez Raspberry Pi egykártyás számítógépet választottam, a rendszert működtető programot Python3 nyelven szerkesztettem. A modellhez forrasztás nélküli próbapanelt választottam, amit a Pi 40 tűs GPIO-jához egy T-csatlakozóval illesztettem.

#### Az elgondolás megvalósításához szükséges elemek kiválasztása
* Termodinamikai szenzor

A macska testhőjének érzékelését egy PIR passzív infra hőérzékelővel oldottam meg. [PIRMINI3](https://github.com/vassb76/RSLRCV_MEMS/blob/master/PIRMINI-3_EN_10038315.pdf) 
![PIR](https://github.com/vassb76/RSLRCV_MEMS/blob/master/PIRMINI3.jpg)

* Mechanikai szenzor

A macska testtömegét egy 5kg terhelhetőségű mérlegcellával mértem. [Mérlegcella](https://github.com/vassb76/RSLRCV_MEMS/blob/master/datasheet-3133.pdf) 

A mért érték egy HX711 alapú I2C interfészes 24 bites ADC-n keresztül jut el a Raspberry-hez. [HX711](https://github.com/vassb76/RSLRCV_MEMS/blob/master/hx711_english.pdf) 

![Mérleg](https://github.com/vassb76/RSLRCV_MEMS/blob/master/Merleg5kg.jpg)
![HX711](https://github.com/vassb76/RSLRCV_MEMS/blob/master/HX711.jpg)

* Aktuátor

A lapátkerék mozgatását egy 4 fázisú unipolár léptetőmotorral valósítottam meg. [Stepper](https://github.com/vassb76/RSLRCV_MEMS/blob/master/28BYJ-48.pdf) 

A motor vezérlését egy ULN2003 alapú meghajtó PCB végzi. [ULN2003](https://github.com/vassb76/RSLRCV_MEMS/blob/master/ULN2003A-PCB.pdf) 

![Stepper](https://github.com/vassb76/RSLRCV_MEMS/blob/master/Stepper.jpg)
![ULN2003](https://github.com/vassb76/RSLRCV_MEMS/blob/master/ULN2003.jpg)

### 3. A modell fizikai összeállítása

A tápadagoló prototípus összeállításának megtervezését a Fritzing (https://fritzing.org/home/) alkalmazással készítettem el. Az összetevők áramfelvétele nem tette szükségesség külső táp beépítését, a Raspberry két 5V-os, illetve egy 3,3V-os tápcsatlakozója elégséges volt a prototípus működéséhez.

![Fritzing](https://github.com/vassb76/RSLRCV_MEMS/blob/master/MEMS4b_bb.png)

A Fritzing-ben megtervezett modell tényleges megvalósítása:

![Proto](https://github.com/vassb76/RSLRCV_MEMS/blob/master/Protot%C3%ADpus.png)


### 4. A prototípust működtető kód

A modell működtetését Python3-ban írt kóddal valósítottam meg, Raspbian Buster operációs rendszer alatt. A kódban felhasználásra került a HX711 ADC-hez Marcel Zak által megírt függvénykönyvtár ([link](https://github.com/gandalf15/HX711)).
Az ötletadó műzliadagoló 6-os osztású lapátkerékkel működik, így a kódban is 6 tömegkategóriát határoztam meg. Az adagok a táp ajánlása alapján lettek meghatározva, ami megadja, hogy mennyi táp az ideális testömeg kg-onként naponta.

