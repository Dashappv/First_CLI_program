# First_CLI_program

""" Using argparse I created a CLI program which requires 4 mandatory arguments and one optional flag.
    The program finds input file that should be modified, in my case replacing one symbol by another in entire file, 
    and creates/saves modified output file. 
    If the flag -u is set, additionaly to replacing symbols, entire text in output file will be printed in uppercase. 

    Example of command line in terminal that will call the program:
    C:\PATH>python modifying_input_file.py -u -i my_input.txt -o output.txt --original_symbol o --replacement_symbol !

    Note:
    my_input.txt should already exist in the same directory as the code
    output.txt can be created while running the program, the name can be set by calling the programm 
    after --original_symbol insert a symbol that should be modified from your input file
    after --replacement_symbol insert a symbol that replaces original symbol
    -u is a flag that prints the text in uppercase. It can be ignored if such modification is not desired """
    
