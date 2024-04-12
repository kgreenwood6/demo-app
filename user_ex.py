import streamlit as st
import csv
import boto3
import io

def collect_feedback(name, NPS, like1, text_feedback, bucket_name):
    # Write the feedback to a CSV file in memory
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(['Name', 'NPS', 'Liked', 'Feedback'])
    writer.writerow([name, NPS, like1, text_feedback])

    # Upload the CSV file to S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key='feedback.csv', Body=csv_buffer.getvalue())

def main():
    st.title("Book Club Feedback")
    st.write("Please let us know how your experience was")

    name = st.text_input("Name or Alias")
    NPS = st.slider("Rate your experience: 0 is the WORST experience and 10 is the BEST", min_value=0, max_value=10, step=1)
    like1 = st.text_input("What did you like most about the app?")
    text_feedback = st.text_input("Any additional feedback")

    if st.button("Submit"):
        # Replace 'your_bucket_name' with your actual S3 bucket name
        bucket_name = 'cse-group-project'
        collect_feedback(name, NPS, like1, text_feedback, bucket_name)
        st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()
