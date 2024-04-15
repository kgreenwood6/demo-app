import streamlit as st
import csv
import os

def collect_feedback(name, NPS, like1, text_feedback):
    # For local saving
    with open('feedback.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, NPS, like1, text_feedback])

    # For saving in the GitHub repo
    repo_path = '/home/ubuntu/demo-app/demo-app/'  # Replace with the actual path to your GitHub repo
    file_path = os.path.join(repo_path, 'feedback.csv')
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'NPS', 'Liked', 'Feedback'])

    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
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
