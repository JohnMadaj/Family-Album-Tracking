import csv

def file_reader(path):
    with open('family_album_tracking.tsv', 'r') as tsvfile:
        # Create a TSV reader
        tsvreader = csv.reader(tsvfile, delimiter='\t')
        next(tsvreader)
        # Loop through each line in the file
        for line in tsvreader:
            # Extract the values from the line
            week_number = line[0]
            # date = line[1]
            # dad = line[2]
            # mom = line[3]
            # jen = line[4]
            # justin = line[5]
            # patrick = line[6]
            # jack = line[7]
            # joey = line[8]
            # jakob = line[9]

            # Add the values to the appropriate family member's dictionary
            dad_dict[week_number] = scan_album(line[2])
            mom_dict[week_number] = scan_album(line[3])
            jen_dict[week_number] = scan_album(line[4])
            justin_dict[week_number] = scan_album(line[5])
            patrick_dict[week_number] = scan_album(line[6])
            jack_dict[week_number] = scan_album(line[7])
            joey_dict[week_number] = scan_album(line[8])
            jakob_dict[week_number] = scan_album(line[9])

def scan_album(column):
    column = column.split(" - ")
    artist = column[0]
    if len(column) == 2:
        album = column[1]
        return [artist, album]
    return artist


# Declare dictionaries for each family member
dad_dict = {}
mom_dict = {}
jen_dict = {}
justin_dict = {}
patrick_dict = {}
jack_dict = {}
joey_dict = {}
jakob_dict = {}

fam_list = [dad_dict, mom_dict, jen_dict, justin_dict, patrick_dict, jack_dict, joey_dict, jakob_dict]


if __name__ == '__main__':
    # file_reader("family_album_tracking.tsv")
    for num, album in justin_dict.items():
        print(num, album)