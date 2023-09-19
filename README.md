# N_remover
A python script designed to remove all rows containing the "|N|" string in a .csv file. Specifically designed for use with SNP count matrix files, wherein erroneous SNPs are generated due to a reference-gene mismatch during SNP calling with metaSNV. The script is very simple, and can be edited to remove other rows with set strings of interest.  

To use, first open the .py file. On line "input_files =", set input equal to the path to the CSV file to be edited. Similarly, set "output_files =" equal to the output name (and/or location) of your choosing. 
To run, simply type: python3 N_remover.py, and press enter. 
