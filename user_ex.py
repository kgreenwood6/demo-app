import streamlit as st
import pandas as pd
import os

def collect_feedback(name, NPS, like1, text_feedback):
    feedback_data = {
        'Name': [name],
        'NPS': [NPS],
        'Liked Most': [like1],
        'Additional Feedback': [text_feedback]
    }

    feedback_df = pd.DataFrame(feedback_data)

    # Check if the CSV file exists
    if not os.path.exists('feedback.csv'):
        # If it doesn't exist, create a new CSV file and write the DataFrame to it
        feedback_df.to_csv('feedback.csv', index=False)
    else:
        # If it exists, append the DataFrame to the existing CSV file
        feedback_df.to_csv('feedback.csv', mode='a', header=False, index=False)

def main():
    st.title("Book Club Feedback")
    st.write("Please let us know how your experience was")

    name = st.text_input("Name or Alias")
    NPS = st.slider("Rate your experience: 0 is the WORST experience and 10 is the BEST", min_value=0, max_value=10, step=1)
    like1 = st.text_input("What did you like most about the app?")
    text_feedback = st.text_input("Any additional feedback")

    if st.button("Submit"):
        collect_feedback(name, NPS, like1, text_feedback)
        st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()
