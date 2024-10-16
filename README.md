# Japanese Tables
...or alphabets

Small program to help me learn hiragana (and soon katakana).
Forked from my very first program teaching [multiplication tables](https://github.com/Loloweb/MultiplicationTables), which is itself inspired by a lost old GWBASIC program.

The idea is to take the algorithm that I used for multiplication tables and use it to learn hiragana. In this case, you could interpret the 2 caracters as an operation that you would have to solve by typing the meaning in romanji. For example, the program might show "あい" and the user will have to type "ai".

Below is a description of the algorithm as it was used for multiplication:

It is most useful when the pupil already knows the tables **in order** and has to learn them at random.
At this stage it is difficult for parents or teachers to question the student in a really random way and without forgetting any operation or ask for the same operation too often. As it must be done agin and again, it can quickly become a chore for them and for the pupil.
This program should make this learning less painful. I could see from first hand experience that it was rather effective.

The idea is not to ask twice an operation when it is correctly answered at the first time, as it is assumed to be *known*. If not, then it will take 2 consecutive correct answers for this operation to be considered as *known*. *Consecutive* for this operation but probably separated by other operations because they are asked randomly chosen among the remaining *unknown* operations.
This algorithm will, at the end, ask repeatedly the same *"unknown"* operations. Repetition leads to memorization.

At the end, the time/operation score is displayed and then, one by one, the operations that were not answered right at first time.

Written and tested only on Windows but should be easy to port to Linux, etc. (Remove the colorama module and port the winsound lines.)

Important: 
- This script runs in console mode only. 
- It is recommended to launch it in full screen and with a BIG POLICE, typically "Consolas" 36 or 72 on Windows 10. On Windows this is done with a shortcut on the Desktop: right-click -> Properties -> Font tab
- You must pass the width and height of the console window as arguments on the command line. Example: `multiplication_tables.py 69 22` . On Windows you can see these values with right-click on the shortcut, Properties -> Layout: Window size
