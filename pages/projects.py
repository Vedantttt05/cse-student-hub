
import streamlit as st
from datetime import date

from database.db import (
    init_projects_table,
    add_project,
    get_projects,
    update_project,
    delete_project
)

# Initialise database
init_projects_table()

# Page heading
st.title("🚀 Project Tracker")

st.write(
    "Plan, organise and monitor your engineering projects."
)

st.divider()

# Project options
statuses = ["Planning", "In Progress", "Completed"]
priorities = ["Low", "Medium", "High"]

# ==================================
# ADD NEW PROJECT
# ==================================

st.header("Create New Project")

with st.form("project_form"):

    project_name = st.text_input("Project Name")

    description = st.text_area(
        "Project Description",
        height=120
    )

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "Start Date",
            value=date.today(),
            key="new_start"
        )

    with col2:
        end_date = st.date_input(
            "Expected Completion Date",
            value=date.today(),
            key="new_end"
        )

    status = st.selectbox(
        "Project Status",
        statuses
    )

    priority = st.selectbox(
        "Project Priority",
        priorities
    )

    technologies = st.text_input(
        "Technologies Used",
        placeholder="Python, SQLite, Streamlit"
    )

    progress = st.slider(
        "Project Progress (%)",
        min_value=0,
        max_value=100,
        value=0
    )

    submitted = st.form_submit_button("Add Project")

    if submitted:

        if not project_name.strip():
            st.error("Please enter a project name.")

        elif end_date < start_date:
            st.error("End date cannot be before start date.")

        elif status == "Completed" and progress != 100:
            st.error("Set progress to 100% for completed projects.")

        else:

            add_project(
                project_name.strip(),
                description.strip(),
                start_date.isoformat(),
                end_date.isoformat(),
                status,
                priority,
                technologies.strip(),
                progress
            )

            st.success("Project added successfully!")

            st.rerun()


st.divider()

# ==================================
# PROJECT STATISTICS
# ==================================

st.header("Project Overview")

projects = get_projects()

total = len(projects)

completed = sum(
    1 for project in projects
    if project[5] == "Completed"
)

in_progress = sum(
    1 for project in projects
    if project[5] == "In Progress"
)

planning = sum(
    1 for project in projects
    if project[5] == "Planning"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Projects", total)
col2.metric("Completed", completed)
col3.metric("In Progress", in_progress)
col4.metric("Planning", planning)

st.divider()

# ==================================
# DISPLAY PROJECTS
# ==================================

st.header("My Projects")

if not projects:

    st.info("No projects available. Add your first project!")

else:

    for project in projects:

        (
            project_id,
            name,
            description,
            start_date,
            end_date,
            status,
            priority,
            technologies,
            progress
        ) = project

        with st.expander(f"🚀 {name} — {status}"):

            st.write("**Description:**")
            st.write(description or "No description provided.")

            st.write(f"**Start Date:** {start_date}")
            st.write(f"**Expected End Date:** {end_date}")
            st.write(f"**Priority:** {priority}")
            st.write(f"**Technologies:** {technologies or 'Not specified'}")

            st.write(f"**Progress: {progress}%**")

            st.progress(progress / 100)

            st.divider()

            # ==================================
            # EDIT PROJECT
            # ==================================

            st.subheader("Edit Project")

            with st.form(f"edit_project_{project_id}"):

                new_name = st.text_input(
                    "Project Name",
                    value=name,
                    key=f"name_{project_id}"
                )

                new_description = st.text_area(
                    "Description",
                    value=description or "",
                    key=f"description_{project_id}"
                )

                new_start = st.date_input(
                    "Start Date",
                    value=date.fromisoformat(start_date),
                    key=f"start_{project_id}"
                )

                new_end = st.date_input(
                    "End Date",
                    value=date.fromisoformat(end_date),
                    key=f"end_{project_id}"
                )

                new_status = st.selectbox(
                    "Status",
                    statuses,
                    index=statuses.index(status),
                    key=f"status_{project_id}"
                )

                new_priority = st.selectbox(
                    "Priority",
                    priorities,
                    index=priorities.index(priority),
                    key=f"priority_{project_id}"
                )

                new_technologies = st.text_input(
                    "Technologies",
                    value=technologies or "",
                    key=f"tech_{project_id}"
                )

                new_progress = st.slider(
                    "Progress (%)",
                    0,
                    100,
                    value=progress,
                    key=f"progress_{project_id}"
                )

                save_changes = st.form_submit_button(
                    "Save Changes"
                )

                if save_changes:

                    if not new_name.strip():
                        st.error("Project name is required.")

                    elif new_end < new_start:
                        st.error("End date cannot be before start date.")

                    elif new_status == "Completed" and new_progress != 100:
                        st.error("Completed projects must have 100% progress.")

                    else:

                        update_project(
                            project_id,
                            new_name.strip(),
                            new_description.strip(),
                            new_start.isoformat(),
                            new_end.isoformat(),
                            new_status,
                            new_priority,
                            new_technologies.strip(),
                            new_progress
                        )

                        st.success("Project updated successfully!")

                        st.rerun()

            # ==================================
            # DELETE PROJECT
            # ==================================

            if st.button(
                "Delete Project",
                key=f"delete_{project_id}"
            ):

                delete_project(project_id)

                st.success("Project deleted successfully!")

                st.rerun()
