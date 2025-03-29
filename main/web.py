
#package for creating webapp
import streamlit as st
import functions
todos = functions.get_todos()
#so a title function returns a title instance (on the webapp)
#order matters

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


#st.session_state displays values  of all session state variables
#without needing a key
st.session_state
print("Hello")