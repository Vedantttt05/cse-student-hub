import streamlit as st

pages = [
    st.Page(
        "pages/dashboard.py",
        title="Student Hub",
        icon="🎓",
        default=True
    ),

    st.Page(
        "pages/assignments.py",
        title="Assignments",
        icon="📝"
    ),

    st.Page(
        "pages/notes.py",
        title="Notes",
        icon="📚"
    ),

    st.Page(
        "pages/projects.py",
        title="Projects",
        icon="🚀"
    )
]

navigation = st.navigation(pages)

navigation.run()