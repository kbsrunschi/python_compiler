###README###
To run, simply run the command 'make file={your file}', where {your file}
is the name of the file you wish to compile WITHOUT the file extension.
E.g. to compile /test/erato.c, use the command 'make file=./test/erato'

Running this command will pre-process the file and create an output in the /test/ folder with a .s extension that contains the assembly code. The print statements to the console are not the generated assembly code. 