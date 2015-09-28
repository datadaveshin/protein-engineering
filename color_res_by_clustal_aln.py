import color_by_score as col

def seq_list_from_file(name_of_file):
    """ 
    Read in the contents of the alignment file line by line.
    (Proper way to open and read each line found here:
    http://stackoverflow.com/questions/8009882/
    how-to-read-large-file-line-by-line-in-python)

    Remove the first few lines.

    Make a dictionary from the remaining. 
    """
    with open(name_of_file) as f:

        list_of_seqs = []
        for line in f:
            # checks to see if top line containing "ClUSTAL" or a blank line
            if line.split(' ', 1)[0] == "CLUSTAL":
                print "this had clustal"
            elif line[0] == ("\n"):
                print "starts blank"
            elif line[0] == (" "):
                print "starts space"
                #print line[0]
                # then make list from remaining
            else:
                term = line[0]
                print "term" + term + "term"
                #print line[0]
                list_of_seqs.append(line.split(None, 10)[1])
        return list_of_seqs
        
def calc_conservation(list_of_seqs):
    """
    Takes a list of sequences, uses the top sequence as a reference,
    then calculates the percentage of residues that are identical to the
    reference residues.
    """
    # remove the first sequence in the list to keep as a reference
    ref_seq = list_of_seqs.pop(0)
    #print ref_seq
    
    # define variables:
    # get number of remaining seqs
    # start a counter to determine the actual residue positions of ref_seq 
    # as we need to account for "-" in the alignments 
    # initialize the list to return that contains the one-letter residue code,
    # the residue position 
    num_seqs = len(list_of_seqs)
    residue_position = 0
    list_of_conservation_scores = []
        
    # iterate over each position in the alignment
    for idx in range(len(ref_seq)):
        
        # first test if the position in refseq is "-" and if not go on
        if ref_seq[idx] != "-":
            residue_position += 1
             
            # iterate through sequences in same position, calculate scores
            total_score = 0 
            for seq in list_of_seqs:
                if seq[idx] == ref_seq[idx]:
                    score = 1
                else: 
                    score = 0
                total_score += score
            percent_conserved = float(total_score) / num_seqs
            list_of_conservation_scores.append((ref_seq[idx], residue_position, percent_conserved))
        # return a tuple with actual amino acid sequence and score 
    return list_of_conservation_scores
    
def output_color_commands(input_list):
    for tup in input_list:
        col.color_by_score(tup[1], tup[2])
        
def test_seq_lengths(alist):
    for item in alist:
        print len(item)

def color_res_by_clustal_aln(clustal_alignment):
    list_of_sequences = seq_list_from_file(clustal_alignment)
    conservation_list = calc_conservation(list_of_sequences)
    output_color_commands(conservation_list)
    
list_of_sequences = seq_list_from_file("pepck-fasta_90-40-115-85.aln")

#test_seq_lengths(list_of_sequences)

conservation_list = calc_conservation(list_of_sequences)
output_color_commands(conservation_list)

#print conservation_list

# print list_of_sequences