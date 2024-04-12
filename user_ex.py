import streamlit as st
import csv

def collect_feedback(name, NPS, like1, text_feedback):
    # For local saving
    with open('feedback.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, NPS, like1, text_feedback])

    # For saving in the GitHub repo
    # Assuming your GitHub repo is already cloned in the EC2 instance
    # Replace 'path_to_your_repo' with the actual path to your GitHub repo
    with open('/home/ubuntu/demo-app/demo-app/feedback.csv', 'a', newline='') as f:
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
