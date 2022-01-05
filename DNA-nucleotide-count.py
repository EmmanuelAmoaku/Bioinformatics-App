import pandas as pd
import streamlit as st
import altair as alt

st.write("""

	# DNA Nucleotide Count Web App

	This app counts the nucleotide composition of query DNA!

	***
	""")


############
# Input Text Box
############

st.header('Enter DNA Sequence')

sequence_input = "DNA Query\nGACCCCCCAAAAGTAGCGATTTGACGTAAAGCCCCAAATTCGAT"

sequence = st.text_area("Sequence Input", sequence_input, height=250) # Displaying the query DNA ina text box
sequence = sequence.splitlines()   # split lines in query DNA if any
sequence = sequence[1:] #Skip the first line 
sequence = ''.join(sequence) # concatenate list to string

st.write("""

	***

""")


## Prints the input DNA sequence
st.header("""

	INPUT (DNA Query)

""")

sequence

st.write("""

	***

""")


## DNA Nucleotide Count
st.header("""

	OUTPUT (DNA Nucleotide Count)

""")


 ##  Obtaining a dictionary of nucleotides and their value counts
def DNA_nucleotide_count(seq):
	d = dict([

		('A', seq.count('A')),
		('T', seq.count('T')),
		('G', seq.count('G')),
		('C', seq.count('C')),
		])
	return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())


## Display Dataframe
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'COUNT'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'NUCLEOTIDE'})
st.write(df)


## Print Text
st.write(" There are" ' ' + str(X['A']) + ' ' "adenine (A)")
st.write(" There are" ' ' + str(X['T']) + ' ' "thymine (T)")
st.write(" There are" ' ' + str(X['G']) + ' ' "guanine (G)")
st.write(" There are" ' ' + str(X['C']) + ' ' "cytosine (C)")


# Plot a bar chart of the nucleotide count
st.subheader('Nucleotide Count Chart')
p = alt.Chart(df).mark_bar().encode(x='NUCLEOTIDE', y='COUNT')
p = p.properties(width=alt.Step(80))   #sets the bar width to 80
st.write(p)



