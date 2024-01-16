import streamlit as st

# Declare Variables
textOutput = ""

# Page config
st.set_page_config(page_title="Number Factorer",layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("Number Factorer")
    st.subheader("Input a number into the box below to receive the factors of that number.")

# Text input box and submit button    
    textInput = st.text_input("Type the number you want to factor here:")
    submit = st.button("Factor")
    st.write("Factors of the inputted number:")

# Programming portion
if submit == True:
    number = textInput
        
    try:
        number = int(number)
    except: 
        textOutput = "Please input a natural number."

    if isinstance (number, int):
        n = number
        x = []

        if number > 10000000:
            textOutput = "Please input a number less than 100,000,000."

        elif number <= 0:
            textOutput = "Please input a number greater than 0"
            
        else:
            for i in range (1, number + 1):
                if number % i == 0:
                    x.append(i)
            textOutput = "The factors of {nTemp} are: {xTemp}".format(nTemp = n, xTemp = x)

container = st.container(border=True)
container.write(textOutput)

# What is a factor?
st.subheader("What is a Factor?")
st.write(

"""
A factor of a number is an integer that, when multiplied by another integer, equals
 the original number. For example, if your original number is 64, a factor of it is 4 
 since it can be multiplied by another integer, 16, to yield the original number of 64. 
 The full list of factors for 64 would be: [1, 2, 4, 8, 16, 32, 64]. Every number in the 
 list has a corresponding value, such that when multiplied by the associated number, it 
 results in the original number of 64.. Factors can also be negative; for example, -4 
 and -16 can be multiplied to obtain the original 64. The original number can also be 
 negative, having one negative and one positive factor to yield the original number. 
 However, this calculator does not support negative values, as they are redundant and 
 self-explanatory.
"""

)

# Why are factors useful? 
st.subheader("Why are factors useful?")
st.write(

"""
Factors can be useful for a wide variety of different things. A simple example would be 
finding ways to evenly distribute something. If you have 64 cookies to give out, you may want
 to know how many cookies to give out and to how many people. By finding the factors of 64: 
 [1, 2, 4, 8, 16, 32, 64], you can see that you are able to give out 1 cookie to 64 people, 
 or 2 cookies to 32 people, 4 cookies to 16 people, and so on. Other potential uses of factors 
 include event planning with a specific number of attendees in a designated format, solving 
 quadratic equations, resource allocation, and more.
"""

)