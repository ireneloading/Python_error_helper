# Coding Problem Explainer
# Use to aid beginners with python specifically if an variable matches everywhere
import streamlit as st

# Beginner error explanations
error_explanations = {
    "SyntaxError: expected ':'": {
        "explanation": "Python expected a colon (:) at the end of a line that starts a block such as if, for, or else.",
        "example": "Wrong: if x > 5\nCorrect: if x > 5:",
        "tip": "When writing conditions or loops (if, for, while, else, elif), always put a colon (:) at the end of the line."
    },
    "IndentationError: expected an indented block": {
        "explanation": "You need to indent (moved to the right) the code that comes after structures like 'if', 'for', or 'while' that end in a ':'.",
        "example": "Wrong:\nif x > 5:\nprint(x)\nCorrect:\nif x > 5:\n    print(x)",
        "tip": "After any line that ends with : press Enter, then Tab (a space) before writing the next line of code."
    },
    "NameError: name 'x' is not defined": {
        "explanation": "You're trying to use a variable that hasn't been defined yet.",
        "example": "Wrong: print(x)\nCorrect: x = 10\nprint(x)",
        "tip": "Make you've assigned values to variables before using them."
    }}
st.title("Beginner-Friendly Python Error Helper")

user_input = st.text_area("Paste your Python error message below and click Submit to get a beginner-friendly explanation:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter an error message before submitting.")
    else:
        matched = False
        for error, details in error_explanations.items():
            if error in user_input:
                st.success("Found a match!")
                st.subheader("Explanation:")
                st.write(details["explanation"])
                st.subheader("Example Fix:")
                st.code(details["example"])
                st.subheader("Helpful Tip:")
                st.write(details["tip"])
                matched = True
                break
        if not matched:
            st.warning("Sorry! This tool currently supports only a few common beginner errors.")
