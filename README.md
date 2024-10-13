# HELLO-ADA-PROJECT

In this project, there was an attempt to develop a simple AI tool using the NLP library TextBlob, to facilitate users to move a basic element/character on the screen using text commands such as 'left', 'right', 'jump', and 'change' (to change color). The user interface has been created using PyGame and the code was entirely written in Python as required.

Besides doing the above, this code also allows for using the arrow keys to move the character while the 'c' key on the user's keyboard will change the character's color.

Running the game is simple. You clone this repository and open in VSCode, PyCharm, etc. The file main.py must then be executed and the game starts right away. 

Note: One needs to install python libraries textblob and pygame to run the code successfully. You may use the terminal command line in the code editor(for eg: VSCode) to install them using 'pip'.

# CHALLENGES

1) At present there seems to be an issue with the range of acceptable text commands to move the character or change color. For eg: "move_left" and "left" might be accepted but "turn_left" would not work.

2) The user may also experience difficulty getting the character moving using the text commands occasionally. The arrow keys, especially the "UP" arrow key and the 'c' key to change color, may seem to work more consistently than the rest.


# IMPROVEMENTS

1) Utilize NLP to recognize equivalent terms to pursue the same action. For eg: "alter" for "change", "leap" for "jump".

2) A GUI could be created within the PyGame window, to type in relevant commands on the screen and pursue the required actions.

Thank you for the assignment! Hope the kids love it :D

Look forward to hearing from you soon. 
