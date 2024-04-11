import streamlit as st
import sqlite3

conn = sqlite3.connect('feedback.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS results (
                name TEXT PRIMARY KEY,
                NPS INTEGER,
                like1 TEXT,
                text_feedback TEXT
            )''')



def collect_feedback(name, NPS, like1, text_feedback):
    # Insert feedback into database
    c.execute("INSERT INTO results (name, NPS, like1, text_feedback) VALUES (?, ?, ?, ?)",
              (name, NPS, like1, text_feedback))
    conn.commit()



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
