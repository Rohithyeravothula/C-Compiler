1) roh.txt is the sample C code
2) Program.c is the main source code
3) execute from terminal as "gcc program.c < roh.txt > output.txt" where "<" is for input , ">" is for output
4) roh.txt is input file and output.txt is output file
5) gen.py is modifier of tokens, which will remove extra spaces, tabs from output.txt
6) execute from terminal as "python gen.py < output.txt > tokens.txt"
7) tokens are stored to tokens.txt file