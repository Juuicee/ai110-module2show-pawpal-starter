# Reconfigured app.py using co-pilot in order to create a Streamlit app that connects the Owner, Pet, Task, and Scheduler classes defined in pawpal_system.py. The app allows users to create an owner and pet, add tasks, and generate a schedule for the day. The code includes UI inputs for task details and displays the current tasks and today's schedule.

import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# -------------------
# Initialize state (IMPORTANT)
# -------------------
if "owner" not in st.session_state:
    st.session_state.owner = None

if "pet" not in st.session_state:
    st.session_state.pet = None

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# -------------------
# UI Inputs
# -------------------
st.subheader("Quick Demo Inputs")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])


# -------------------
# Create Owner + Pet
# -------------------
if st.button("Create Owner & Pet"):
    owner = Owner(owner_name)
    pet = Pet(pet_name, species)

    owner.add_pet(pet)

    st.session_state.owner = owner
    st.session_state.pet = pet

    st.success("Owner and pet created!")


# -------------------
# Task Section
# -------------------
st.markdown("### Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)

with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)


# -------------------
# Add Task (CONNECTED)
# -------------------
if st.button("Add task"):
    if st.session_state.pet is None:
        st.error("Create owner and pet first!")
    else:
        task = Task(task_title, date.today())

        st.session_state.pet.add_task(task)
        st.session_state.scheduler.add_task(task)

        # keep UI table too
        st.session_state.tasks.append(
            {"title": task_title, "duration": duration, "priority": priority}
        )

        st.success("Task added!")


# -------------------
# Show tasks
# -------------------
if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet.")


# -------------------
# Generate Schedule (CONNECTED)
# -------------------
st.divider()
st.subheader("Build Schedule")

if st.button("Generate schedule"):
    if st.session_state.owner is None:
        st.error("Create owner and pet first!")
    else:
        scheduler = st.session_state.scheduler
        today_tasks = scheduler.get_tasks_for_day(date.today())

        st.subheader("Today's Schedule")

        if not today_tasks:
            st.info("No tasks scheduled.")
        else:
            for task in today_tasks:
                status = "✅" if task.completed else "❌"
                st.write(f"{task.title} ({status})")
# Suggested approach:
# 1. Design your UML (draft).
# 2. Create class stubs (no logic).
# 3. Implement scheduling behavior.
# 4. Connect your scheduler here and display results.