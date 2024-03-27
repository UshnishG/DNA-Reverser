import streamlit as st
import io
from Bio import SeqIO

def extract_first_dna_sequence_from_fasta(fasta_file):
    with io.TextIOWrapper(fasta_file, encoding="utf-8") as file_wrapper:
        for record in SeqIO.parse(file_wrapper, "fasta"):
            return str(record.seq)
    return None

def reverse_complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_sequence = sequence[::-1]  # Reverse the sequence
    reverse_complement_sequence = ''
    reversed_part = ''
    complemented_part = ''
    for base in reversed_sequence:
        complement_base = complement_dict.get(base, base)
        reverse_complement_sequence += complement_base
        reversed_part += base
        complemented_part += complement_base
    return reverse_complement_sequence, reversed_part, complemented_part


def main():
    st.title("DNA Reverse Complement Tool")

    fasta_file = st.file_uploader("Upload a FASTA file", type=["fasta"])

    if fasta_file:
        first_sequence = extract_first_dna_sequence_from_fasta(fasta_file)

        if first_sequence:
            st.write("### DNA Sequence:")
            st.write(first_sequence)

            reverse_comp_sequence, reversed_part, complemented_part = reverse_complement(first_sequence)
            st.write("### Reverse Complement:")
            st.write(reverse_comp_sequence)
            st.write("### Reversed Part:")
            st.write(reversed_part)
            st.write("### Complemented Part:")
            st.write(complemented_part)
        else:
            st.write("No DNA sequences found in the uploaded FASTA file.")

if __name__ == "__main__":
    main()
