## Python chess v2

This project is my implementation of chess in Python with a UI in command prompt. I built it in summer of 2020. Python was the first language that I took seriously and this project was kind of a testament mostly to myself that I mastered most of the basics.

It has several lackings though. First of all, the gameboard UI is broken for some reason. Perhaps it's because I was working with PyCharm at the time and the output was designed for the PyCharm console. 

Secondly, the UI is certainly lacking. I didn't have any experience in building GUIs back then so command prompt was my only feasible option. I was also kind of lazy to at least implement a normal way of inputting moves i.e. e4 e5 Nf3 d6 etc.

And lastly I didn't implement Castling and En passant. The reason for that is that these mehanics necessitate storing previous states of the game and for only God knows why I thought that I needed a seperate database to store them. I never even considered storing all the moves in a variable, which I'm kind of ashamed of. So I went to learn databases and ultimately never came back to the project. 

If you want to see my progress you can check out my first version of the chess. As far as I remember it was purely functional, not a single class. Here's the link: https://github.com/KissMyUSSR/Python-chess-v1