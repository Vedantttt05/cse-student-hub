
import streamlit as st

from database.db import (
    init_notes_table,
    add_note,
    get_notes,
    update_note,
    delete_note
)

# Initialise notes database table
init_notes_table()

# Page heading
st.title("📚 Notes Management")
st.write("Create, organise, search and manage your study notes.")

st.divider()

# Add a new note
st.header("Create New Note")

with st.form("add_note_form"):

    title = st.text_input("Note Title")

    subject = st.selectbox(
        "Select Subject",
        [
            "Python Programming",
            "Computer Networks",
            "Operating Systems",
            "Database Management",
            "Cybersecurity",
            "Other"
        ]
    )

    content = st.text_area(
        "Write Your Notes",
        height=180,
        placeholder="Write your study notes here..."
    )

    submitted = st.form_submit_button("Save Note")

    if submitted:

        if title.strip() and content.strip():

            add_note(
                title.strip(),
                subject,
                content.strip()
            )

            st.success("Note saved successfully!")
            st.rerun()

        else:
            st.error("Please enter a title and note content.")

st.divider()

# Display saved notes
st.header("Your Saved Notes")

notes = get_notes()

# Search notes
search = st.text_input(
    "🔍 Search Notes",
    placeholder="Search by title, subject or content..."
)

# Subject filter
subjects = sorted(set(note[2] for note in notes))

selected_subject = st.selectbox(
    "Filter by Subject",
    ["All Subjects"] + subjects
)

# Filter notes
filtered_notes = []

for note in notes:

    note_id, title, subject, content, created_at = note

    matches_search = (
        search.lower() in title.lower()
        or search.lower() in subject.lower()
        or search.lower() in content.lower()
    )

    matches_subject = (
        selected_subject == "All Subjects"
        or subject == selected_subject
    )

    if matches_search and matches_subject:
        filtered_notes.append(note)


st.caption(f"Showing {len(filtered_notes)} of {len(notes)} notes")

# Display notes
if not filtered_notes:

    st.info("No matching notes found. Create a new note above!")

else:

    for note in filtered_notes:

        note_id, title, subject, content, created_at = note

        with st.expander(f"📖 {title} — {subject}"):

            st.caption(f"Created: {created_at}")

            st.write(content)

            st.divider()

            # Edit note
            with st.form(f"edit_note_{note_id}"):

                st.subheader("Edit Note")

                new_title = st.text_input(
                    "Note Title",
                    value=title,
                    key=f"title_{note_id}"
                )

                new_subject = st.text_input(
                    "Subject",
                    value=subject,
                    key=f"subject_{note_id}"
                )

                new_content = st.text_area(
                    "Note Content",
                    value=content,
                    height=150,
                    key=f"content_{note_id}"
                )

                save_changes = st.form_submit_button(
                    "Save Changes"
                )

                if save_changes:

                    if new_title.strip() and new_subject.strip() and new_content.strip():

                        update_note(
                            note_id,
                            new_title.strip(),
                            new_subject.strip(),
                            new_content.strip()
                        )

                        st.success("Note updated successfully!")
                        st.rerun()

                    else:
                        st.error("All fields are required.")

            # Delete note
            if st.button("Delete Note", key=f"delete_{note_id}"):

                delete_note(note_id)

                st.success("Note deleted successfully!")
                st.rerun()
