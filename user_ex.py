import streamlit as st
import csv
import os

def collect_feedback(name, NPS, like1, text_feedback):
    # Define the directory to save the CSV file
    save_directory = 'C:\Users\green\OneDrive\Documents\Georgia Tech\CSE6242\'  # Replace with the desired directory

    # Ensure that the directory exists, create it if it doesn't
    os.makedirs(save_directory, exist_ok=True)

    # Write the feedback to the CSV file
    csv_file = os.path.join(save_directory, 'feedback.csv')
    with open(csv_file, 'a', newline='') as f:
        writer = csv.writer(f)
        # If the file is empty, write the header row
        if os.stat(csv_file).st_size == 0:
            writer.writerow(['Name', 'NPS', 'Liked', 'Feedback'])
        # Write the feedback data
        writer.writerow([name, NPS, like1, text_feedback])

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
