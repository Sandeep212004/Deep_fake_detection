import streamlit as st
import json
import os

# Set the page configuration (title and layout)
st.set_page_config(page_title="History", layout="centered")

# Display the title in the center of the page using HTML styling
st.markdown(
    "<h2 style='text-align: center;'>📜 Detection History</h2>",
    unsafe_allow_html=True
)

# Define the path to the history file
history_file = "history.json"

# Check if the history file exists
if os.path.exists(history_file):
    try:
        # Open and read the history data from the JSON file
        with open(history_file, "r") as file:
            history_data = json.load(file)

        # Check if the file is empty
        if not history_data:
            st.info("There are no records in the history file yet.")
        else:
            # Iterate through the history entries in reverse order (most recent first)
            for record in reversed(history_data):
                st.markdown("### 📂 File Details")
                st.markdown(f"- **Type**: `{record['type']}`")
                st.markdown(f"- **Filename**: `{record['filename']}`")
                st.markdown(f"- **Result**: `{record['result']}`")
                st.markdown(f"- **Timestamp**: `{record['timestamp']}`")

                # Display associated media if file path is saved and the file exists
                if "filepath" in record:
                    if os.path.exists(record["filepath"]):
                        # Display image if the type is Image
                        if record["type"] == "Image":
                            st.markdown("#### 🖼️ Image Preview")
                            st.image(record["filepath"], caption="Detected Image", use_column_width=True)

                        # Display video if the type is Video
                        elif record["type"] == "Video":
                            st.markdown("#### 🎥 Video Preview")
                            st.video(record["filepath"])
                    else:
                        st.warning(f"The file at `{record['filepath']}` could not be found.")
                else:
                    st.warning("No file path available for preview.")

                st.markdown("<hr style='border-top: 1px solid #bbb;'>", unsafe_allow_html=True)

    except json.JSONDecodeError:
        st.error("Failed to load history. The file may be corrupted or not in JSON format.")
else:
    st.info("No history file found. Run some detections first to create one.")

# Optionally suppress deprecation warning from unsafe HTML
st.markdown("""
<style>
    .st-emotion-cache-1v0mbdj.e115fcil1 {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)
