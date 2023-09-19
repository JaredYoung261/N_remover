import csv

# Define the input and output file paths
input_file = 'metaSNV_count_matrix.csv'
output_file = 'nfilt_metaSNV_count_matrix.csv'

# Open the input CSV file for reading and the output CSV file for writing
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV reader and writer
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Iterate through each row in the input CSV
    for row in reader:
        # Check if the row contains "|N|", and skip it if it does
        if "|N|" in ','.join(row):
            continue

        # If not, write the row to the output CSV
        writer.writerow(row)

print("Rows containing '|N|' removed. Output saved to 'nfilt_metaSNV_count_matrix.csv'")