
import streamlit as st
from datetime import date

from database.db import (
    init_db,
    add_assignment,
    get_assignments,
    update_assignment,
    delete_assignment
)

# Initialise database
init_db()

# Page heading
st.title("📝 Assignment Manager")
st.write("Add, manage and track your college assignments.")

st.divider()

# Add assignment form
st.header("Add New Assignment")

with st.form("assignment_form"):

    title = st.text_input("Assignment Name")

    subject = st.text_input("Subject")

    due_date = st.date_input(
        "Submission Deadline",
        value=date.today()
    )

    submitted = st.form_submit_button("Add Assignment")

    if submitted:
        if title.strip() and subject.strip():

            add_assignment(
                title.strip(),
                subject.strip(),
                due_date.isoformat()
            )

            st.success("Assignment added successfully!")
            st.rerun()

        else:
            st.error("Please enter both assignment name and subject.")

st.divider()

# Retrieve assignments
st.header("Your Assignments")

assignments = get_assignments()

# Calculate statistics
total = len(assignments)
completed = sum(row[4] for row in assignments)
pending = total - completed

col1, col2, col3 = st.columns(3)

col1.metric("Total", total)
col2.metric("Completed", completed)
col3.metric("Pending", pending)

st.divider()

# Display assignments
if not assignments:
    st.info("No assignments yet. Add your first assignment above!")

else:
    for assignment in assignments:

        assignment_id, title, subject, due_date, completed = assignment

        col1, col2, col3 = st.columns([3, 2, 2])

        with col1:
            st.write(f"**{title}**")
            st.caption(f"Subject: {subject}")

        with col2:
            st.write(f"Deadline: {due_date}")

            if completed:
                st.success("Completed")
            elif date.fromisoformat(due_date) < date.today():
                st.error("Overdue")
            else:
                st.warning("Pending")

        with col3:
            if completed:
                if st.button("Undo", key=f"undo_{assignment_id}"):
                    update_assignment(assignment_id, 0)
                    st.rerun()

            else:
                if st.button("Complete", key=f"complete_{assignment_id}"):
                    update_assignment(assignment_id, 1)
                    st.rerun()

            if st.button("Delete", key=f"delete_{assignment_id}"):
                delete_assignment(assignment_id)
                st.rerun()

        st.divider()
