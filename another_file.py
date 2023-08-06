import pandas as pd
import shutil
import nbformat as nbf
from nbconvert.preprocessors import ExecutePreprocessor
import os

def perform_feature_selection(file,algo):
    # Create a directory for storing uploaded files
    upload_folder = "uploaded_files"
    os.makedirs(upload_folder, exist_ok=True)

    # Save the uploaded file in the folder with a specific name
    uploaded_file_name = os.path.join(upload_folder, "uploaded_file.csv")
    with open(uploaded_file_name, "wb") as f:
        f.write(file.read())
    if algo=='Genetic Algorithm':
        result=execute_notebook("multiobjectiveGeneticAlgorithm.ipynb", uploaded_file_name)
        print("Yes")
    elif algo=='Partical Swarm Optimization':
        print("PSO start")
        result = execute_notebook("pso_self__multiobjective (1).ipynb", uploaded_file_name)
        print("pso end")
    else:
       # Run testBBO2.ipynb through nbconvert and get the result CSV path
       result = execute_notebook("testBBO2.ipynb", uploaded_file_name)

    # Read the result CSV file
    # result = pd.read_csv(result_file)

    # Return the result
    return result

def execute_notebook(notebook_file, input_file):
    # Read the notebook
    with open(notebook_file, "r") as f:
        notebook = nbf.read(f, as_version=nbf.NO_CONVERT)

    # Modify the input file path in the notebook
    for cell in notebook.cells:
        if "uploaded_file.csv" in cell.source:
            cell.source = cell.source.replace("uploaded_file.csv", input_file)

    # Execute the notebook
    ep = ExecutePreprocessor()
    ep.preprocess(notebook)

    # Find the result CSV file path in the notebook outputs
    result_file = pd.read_csv("result.csv")
    return result_file

# if __name__ == "__main__":
#     file = pd.read_csv("your_uploaded_file.csv")  # Replace with your uploaded file
#     result_file = perform_feature_selection(file)

#     if result_file is not None:
#         result = pd.read_csv(result_file)
#         print(result)








