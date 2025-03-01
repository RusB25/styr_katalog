import streamlit as st
from data.default_todos import default_todos

# Set page configuration
st.set_page_config(page_title="W17 driftsättning", layout="wide")

# Initialize session state for each todo if not already set
for group, todos in default_todos.items():
    for todo in todos:
        key = f"{group}_{todo}"
        if key not in st.session_state:
            st.session_state[key] = False

# Page Title
st.title("Checklist")


# Reset Button: Uncheck all todos when clicked
@st.fragment()
def reset_checklist():
    if st.button("Reset"):
        st.session_state.show_confirm_reset = True

    if st.session_state.get("show_confirm_reset", False):
        st.write("Are you sure you want to reset all tasks?")
        if st.button("Yes, reset"):
            for group, todos in default_todos.items():
                for todo in todos:
                    key = f"{group}_{todo}"
                    st.session_state[key] = False
            st.session_state.show_confirm_reset = False
            st.rerun()
        if st.button("Cancel"):
            st.session_state.show_confirm_reset = False
            st.rerun()


reset_checklist()

# Calculate progress
total_todos = sum(len(todos) for todos in default_todos.values())
completed_todos = sum(
    st.session_state[f"{group}_{todo}"]
    for group, todos in default_todos.items()
    for todo in todos
)
progress = completed_todos / total_todos

# Display progress bar with percentage in the sidebar
progress_color = "green" if progress == 1.0 else "blue"
st.sidebar.markdown(
    f"""
    <div style="width: 100%; background-color: lightgray; border-radius: 5px;">
        <div style="width: {progress * 100}%; background-color: {progress_color}; height: 24px; border-radius: 5px;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.sidebar.write(
    f"Progress: {completed_todos}/{total_todos} tasks completed ({progress:.0%})"
)

# Display completion message if all tasks are done
if progress == 1.0:
    st.toast("Congratulations! All tasks are completed.")

# Display todos for each group
for group, todos in default_todos.items():
    st.header(group.capitalize())
    for todo in todos:
        key = f"{group}_{todo}"
        col1, col2 = st.columns([1, 9])
        with col1:
            # Provide a non-empty label and hide it for accessibility
            checked = st.checkbox(
                "Checkbox",
                value=st.session_state[key],
                key=key,
                label_visibility="hidden",
            )
        with col2:
            if st.session_state[key]:
                st.markdown(
                    f"<span style='color: green; font-size: 18px'>{todo}</span>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"<span style='color: #1E90FF; font-size: 18px'>{todo}</span>",
                    unsafe_allow_html=True,
                )
