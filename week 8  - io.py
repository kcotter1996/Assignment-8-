#****************************************************************
#**  Program:    Program 8, File I/O                           **
#**  Programmer: Kiersten Cotter                               **
#**  Date:       02/24/2022                                    **
#****************************************************************

import os                                       # Import opsys
import os.path                                  # Import path functions
from   os import system                         # Import system functions from os

def clrscr( ):                                  # Define clear screen function
    _ = system( 'cls' )
    
loop = True
while loop:
    clrscr( )
    print("* * **********************  Welcome  ********************** * *\n")
    print( "File I/O  "   )
    print( "-----------------------\n" )
    print( "Please enter directory string for saving your file:" )
    print( "\tDo not enter the filename yet.\n" )

    path  = input( "Enter directory: " )        # Wait for user input  
    if not( path.endswith( os.path.sep )):      # If dir NOT end with seperator
        path += os.path.sep                     # Append a seperator

    isdir = os.path.isdir( path )               # Eval if valid dir name
    if not( isdir ):                            # If directory not exist
        os.mkdir( path )                        # Create the directory
            
    fname = input( "Enter filename : " )        # Wait for user input
    fSpec = os.path.join( path, fname )         # fileSpec = dir & fname

    print( "\n" )         
    name   = input( "Enter your name:    " )    # Wait for user input
    addr   = input( "Enter your address: " )    # Wait for user input
    fone   = input( "Enter phone number: " )    # Wait for user input

    with open( fSpec, 'w' ) as file:            # Write out file by line
        file.write( name )
        file.write( ", " )
        file.write( addr )
        file.write( ", " )
        file.write( fone )
        file.write( "\n" )
        file.close( )

    print( "\n----------------------------------------" )
    print( "Content of file: " )

    with open( fSpec, 'r' ) as file:            # Read file content by line
        read_data = file.read( )
        print( read_data )

    loop = input( "Enter another file (Y/N)? : " )# Wait for user input
    if( loop.upper( ) == 'N' ):
        loop = False


exit( )
#*****************  END OF PROGRAM CODE  ********************
