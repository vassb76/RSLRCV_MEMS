# GKLB_INTM020-Mikroelektromechanikai rendszerek tárgy vizsgafeladata.
## Passzív infra mozgásérzékőlős, tömegmérésen alapuló automata tápadagoló.

### 1. Projekt kiválasztása.

Vizsgafeladnak egy testtömeg alapján működő automata száraztáp adagoló berendezés modelljét választottam. Az alapgondolat onnét eredt, hogy családon belül problémát szokott okozni, hogy éppen ki eteti a macskát, miért üres a tányérja, túl sok táp lett kiadagolva, stb. Az adagoló hasonlóan működne gyermekeim forgó lapátkereskes műzli adagoló berendezéséhez. (lsd. 1. kép)![Műzliadagoló](https://github.com/vassb76/RSLRCV_MEMS/blob/master/M%C5%B1zliadagol%C3%B3.png "1. kép Műzliadagoló")

### 2. Hardver és szoftverkörnyezet, szenzorok, motor kiválasztása.

A projekt kivitelezéséhez Raspberry Pi egykártyás számítógépet választottam, a rendszert működtető programot Python3 nyelven szerkesztettem.

#### Az elgondolás megvalósításához szükséges elemek kiválasztása:
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

