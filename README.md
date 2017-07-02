# Picture-Generator

## Description:
The script reads standard input (stdin), converts it to integers and adds it to a set of states that make a pixel, wraping around when it exceeds 255. The script can read any standard input.

## Usage:
The script takes something from stdin and jumbles the internal states accordingly, producing an image as an output.
Execution syntax includes:
> (some stdin) | python picturegen.py

## Arguments:

> -v

Verbosity. Prints 25, 50, 75 and 100% completion of each iteration and some extra messages.

> -i [n]

Number of iterations. Defines how many times the program will produce an output and increases the byte input amount for the internal states.

> -f [directory and name].png

File name. Defines the file directory and name. This will make the program output one file and for each iteration, it will overwrite it.

> -d [directory]

Directory. Places all generated iterations named 1.png to n.png where n is the number of iterations into the specified directory.

> -w [width]
> -h [height]

Define the width and height of the image.

> -nre

No reset. Stops the program from resetting the internal states to 0 after every pixel.
