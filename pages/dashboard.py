
import streamlit as st
import pandas as pd
import plotly.express as px

from datetime import date

from database.db import (
    init_db,
    init_notes_table,
    init_projects_table,
    get_assignments,
    get_notes,
    get_projects
)

# ==================================
# 1. PAGE CONFIGURATION
# ==================================

st.set_page_config(
    page_title="CSE Student Hub",
    page_icon="🎓",
    layout="wide"
)

# Initialise all database tables
init_db()
init_notes_table()
init_projects_table()

# ==================================
# 2. FETCH DATABASE INFORMATION
# ==================================

assignments = get_assignments()
notes = get_notes()
projects = get_projects()

# ==================================
# 3. CALCULATE STATISTICS
# ==================================

total_assignments = len(assignments)

completed_assignments = sum(
    row[4] for row in assignments
)

pending_assignments = (
    total_assignments - completed_assignments
)

total_notes = len(notes)

total_projects = len(projects)

completed_projects = sum(
    1 for project in projects
    if project[5] == "Completed"
)

active_projects = sum(
    1 for project in projects
    if project[5] == "In Progress"
)

# ==================================
# 4. DASHBOARD HEADER
# ==================================

st.title("🎓 CSE Student Hub")

st.subheader(
    "Your Personal Academic Productivity Dashboard"
)

st.write(
    "Monitor your assignments, notes and engineering projects."
)

st.caption(f"Today's Date: {date.today().strftime('%d %B %Y')}")

st.divider()

# ==================================
# 5. MAIN STATISTICS
# ==================================

st.header("📊 Academic Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Assignments",
    total_assignments
)

col2.metric(
    "Completed Assignments",
    completed_assignments
)

col3.metric(
    "Saved Notes",
    total_notes
)

col4.metric(
    "Total Projects",
    total_projects
)

st.divider()

# ==================================
# 6. ASSIGNMENT PROGRESS CHART
# ==================================

st.header("📝 Assignment Progress")

if total_assignments > 0:

    assignment_data = pd.DataFrame({
        "Status": ["Completed", "Pending"],
        "Count": [
            completed_assignments,
            pending_assignments
        ]
    })

    fig = px.pie(
        assignment_data,
        names="Status",
        values="Count",
        title="Assignment Completion"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info("Add assignments to see your progress chart.")

st.divider()

# ==================================
# 7. PROJECT STATUS CHART
# ==================================

st.header("🚀 Project Overview")

if total_projects > 0:

    project_data = pd.DataFrame({
        "Status": ["Planning", "In Progress", "Completed"],
        "Count": [
            sum(1 for p in projects if p[5] == "Planning"),
            active_projects,
            completed_projects
        ]
    })

    fig = px.bar(
        project_data,
        x="Status",
        y="Count",
        title="Projects by Status",
        text="Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:

    st.info("Add projects to see your project overview.")

# ==================================
# 8. UPCOMING ASSIGNMENTS
# ==================================

st.divider()

st.header("⏰ Upcoming Assignments")

today = date.today()

upcoming = []

for assignment in assignments:

    assignment_id, title, subject, due_date, completed = assignment

    if not completed:

        due = date.fromisoformat(due_date)

        upcoming.append({
            "Assignment": title,
            "Subject": subject,
            "Deadline": due,
            "Days Remaining": (due - today).days
        })

upcoming.sort(key=lambda item: item["Deadline"])

if upcoming:

    upcoming_df = pd.DataFrame(upcoming[:5])

    st.dataframe(
        upcoming_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.success("No pending assignments. Great work!")

# ==================================
# 9. PROJECT PROGRESS
# ==================================

st.divider()

st.header("📌 Project Progress")

if projects:

    for project in projects:

        project_id = project[0]
        name = project[1]
        status = project[5]
        progress = project[8]

        st.write(f"**{name}** — {status}")

        st.progress(progress / 100)

        st.caption(f"{progress}% completed")

else:

    st.info("Your project progress will appear here.")

# ==================================
# 10. QUICK SUMMARY
# ==================================

st.divider()

st.header("📚 Your Learning Summary")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Pending Assignments",
        pending_assignments
    )

with col2:

    st.metric(
        "Active Projects",
        active_projects
    )

with col3:

    st.metric(
        "Completed Projects",
        completed_projects
    )

st.success(
    "Your CSE Student Hub dashboard is up to date!"
)
