
filenames = ['base.html', 'cryptindex.html']

# Open file3 in write mode
with open('../Crypto.html', 'w') as outfile:
    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")
