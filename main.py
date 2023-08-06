import streamlit as st
import base64
from another_file import perform_feature_selection
from io import BytesIO

# Custom CSS styles
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #2e86de;
        margin-bottom: 10px;
    }
    .upload-container {
        display: flex;
        justify-content: center;
    }
    .upload-box {
        width: 70%;
        padding: 20px;
        border: 2px dashed #2e86de;
        border-radius: 10px;
        text-align: center;
        color: #2e86de;
        font-size: 20px;
        cursor: pointer;
    }
    .selected-file {
        margin-top: 10px;
        font-size: 18px;
        font-weight: bold;
    }
    .algorithm-selector {
        margin-top: 20px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .button-style {
        background-color: #22a3a0; /* Change the button color to green */
        color: #fff;
        padding: 12px 24px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        margin: 0 10px;
        transition: background-color 0.3s ease;
    }
    .button-style:hover {
        background-color: #F8F8FF; /* Change the hover color to a darker shade of red */
    }
    .result {
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
        overflow-x: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Feature Flex : Adaptive Feature Selection Toolkit")

    # Add an image to the website
    st.image("https://media.licdn.com/dms/image/D4D12AQEvmbuFNHsobA/article-cover_image-shrink_600_2000/0/1687623875560?e=2147483647&v=beta&t=DKZ9ILeRBD4L2SfR5ro3RILV210nMH89rJbXjiTart0", use_column_width=True)

    st.markdown(
        "Welcome to the Feature Selection Toolbox, a powerful tool for optimizing your dataset. Upload a CSV file with integer, real, or categorical values (no text or nulls) and place the target column on the right. Choose from various algorithms for feature selection, view results, and download selected features as a CSV file. Trust our guidelines for accurate and reliable outcomes. Empower your data analysis with this user-friendly and efficient toolbox"
    )

    # File selection
    st.markdown("<div class='header'>File Selection</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(" ", type=["csv"], accept_multiple_files=False, key="file_uploader")
    if uploaded_file:
        st.markdown("<div class='selected-file'>Selected File: " + uploaded_file.name + "</div>", unsafe_allow_html=True)

    # Algorithm selection
    st.markdown("<div class='header algorithm-selector'>Algorithm Selection</div>", unsafe_allow_html=True)
    algorithms = ["Genetic Algorithm", "Biogeography-Based Optimization Algorithm", "Partical Swarm Optimization"]
    selected_algorithm = st.selectbox("Select an algorithm", algorithms)

    # Perform feature selection
    if st.button("Perform Feature Selection", key="perform_btn"):
        if uploaded_file is None:
            st.warning("Please upload a file.")
        else:
            # Send the uploaded file to the another_file.py file
            result = perform_feature_selection(uploaded_file,selected_algorithm)

            # Display the result
            st.markdown("<div class='header result'>Feature Selection Result</div>", unsafe_allow_html=True)
            st.dataframe(result)

            # Download button for the result file
            csv_file = result.to_csv(index=False)
            b64 = base64.b64encode(csv_file.encode()).decode()
            href = f'<a class="button-style" href="data:file/csv;base64,{b64}" download="result.csv">Download Result CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
