import streamlit as st
import subprocess

# Function to save uploaded file to specified path
def save_uploaded_file(uploaded_file, save_path):
    try:
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return st.success(f"Saved file : {uploaded_file.name} to {save_path}")
    except Exception as e:
        return st.error(f"Error saving file : {str(e)}")

# Streamlit UI
st.title("LLM Fine-Tuning and Model Mergin")

# File uploader
uploaded_file = st.file_uploader("Choose a file")

# Text input for specifying save path
save_path = "/Users/you/data/zy/train.jsonl"

# Button to save the file
if st.button("Save File"):
    if uploaded_file is not None and save_path:
        save_uploaded_file(uploaded_file, save_path)
    else:
        st.error("Please upload a file and specify the save path")


# Function to run shell command
def run_shell_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

# Streamlit UI
st.title("Run Shell Command from Streamlit")

# Text input for shell command
command = "./run.sh"

# Button to run the command
if st.button("Fine tuning and merging"):
    with st.spinner("Running command..."):
        stdout, stderr = run_shell_command(command)
        st.success("Command executed successfully!")
        st.subheader("Output:")
        st.text(stdout)
        if stderr:
            st.subheader("Errors:")
            st.text(stderr)
