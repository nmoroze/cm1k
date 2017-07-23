# CM1K Breakout Board
This repo contains the code and design files for the CM1K breakout board discussed in this [blog post](https://medium.com/@noahmoroze/experiments-with-the-cm1k-neural-net-chip-32b2d5ca723b).

## Hardware
Under the `src/` directory I've included the original Altium files for the schematic and PCB, as well the library files for the crystal oscillator and CM1K. I know Altium is fairly inaccessible, but I've had some trouble getting a good export that works in a free PCB editor. Please contact me if you would like to work with these files, and I'll help you make them accessible to your editor of choice!

The `dist/` directory contains a PDF of the schematic as well as a zip file containing Gerber files for the PCB. This zip file is the exact same as the one I uploaded to Advanced Circuits to purchase this board. 

### BOM
I originally purchased all components from Digikey, and generated the BOM below from that cart. However, the CM1K no longer appears to be available from Digikey. 

| Part                               | Quantity | Digkey Part Number | Manufacturer Part Number |
|------------------------------------|----------|--------------------|--------------------------|
| IC REG LDO 1.2V 0.8A SOT223        | 1        | 497-4240-1-ND      | LD1117S12TR              |
| IC REG LDO 3.3V 0.8A DPAK          | 1        | 497-1236-1-ND      | LD1117DT33TR             |
| IC ASIC CHIP CM1K 1024 NEURONS     | 1        | N/A                | N/A                      |
| OSC XO 27.000MHZ HCMOS TTL SMD     | 1        | 535-9263-1-ND      | ASFL1-27.000MHZ-EK-T     |
| RES SMD 270 OHM 5% 1/10W 0603      | 26       | 311-270GRCT-ND     | RC0603JR-07270RL         |
| CAP CER 0.1UF 50V Y5V 0603         | 18       | 311-1343-1-ND      | CC0603ZRY5V9BB104        |
| RES SMD 120 OHM 5% 1/10W 0603      | 2        | 311-120GRCT-ND     | RC0603JR-07120RL         |
| CAP CER 10UF 16V X5R 0603          | 2        | 490-7201-1-ND      | GRM188R61C106MA73D       |
| CAP CER 0.01UF 50V X7R 0603        | 1        | 311-1085-1-ND      | CC0603KRX7R9BB103        |
| LED ORANGE CLEAR 0603 SMD          | 1        | 160-1445-1-ND      | LTST-C191KFKT            |


## Code
The code for this board consists of a small collection of fairly short Python scripts. It's not particularly clean or well documented right now, but most of it is short enough that it should be fairly straightforward. I'm not planning to go back and clean it up unless I decide to pursue a larger project using the CM1K. 

The `code/` directory includes:
- `cm1k.py`, a simple library for accessing the CM1K's hardware from Python 
- `test.py`, a small unit test file containing a simple test script 
- `mnist_test.py`, the script I used to run my MNIST KNN experiment documented in the blog post
- `requirements.txt`, the pip requirements for running `mnist_test`

## Licensing
The hardware design files are licensed under [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/), and the code is provided under the [MIT license](https://opensource.org/licenses/MIT). Original copyright Noah Moroze, 2017.  
