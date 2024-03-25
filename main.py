import streamlit as st



def reverse(dna: str) -> str:
    return dna[::-1]

def complement(dna: str) -> str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(complement[base] for base in dna)

def reverse_complement(dna: str) -> str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_dna = dna[::-1]  # Reverse the DNA sequence
    return "".join(complement[base] for base in reversed_dna)

if __name__ == "__main__":
    st.title("DNA Reverser")

    input_dna = st.text_input("Enter DNA sequence:")

    operation = st.radio("Choose operation:", ("Reverse", "Complement", "Reverse Complement"))

    if st.button("Perform operation"):
        if operation == "Reverse":
            st.write(f"Reverse of the given DNA is : {reverse(input_dna)}")
        elif operation == "Complement":
            st.write(f"Complement of the given DNA is : {complement(input_dna)}")
        else:
            st.write(f"Reverse Complement of the given DNA is : {reverse_complement(input_dna)}")