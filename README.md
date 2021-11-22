# COSC 329 - Assignment #5

### Project Structure

- `data/`
    - Contains the raw data downloaded from the assignment page.
- `processed/`
    - Contains the data after preprocessing/determining ngrams for each sentence in each file. I separated these so they
      each are in their own file relative to their raw data file. It makes it easier to read, and manipulate in future
      code.
- `scripts/`
    - Contains the scripts that are used for pre-processing/determining the ngrams and calculating the containment
      values, then exporting these values to the csv.
- `util/`
    - Contains a helper function to create a new directory if it doesn't already exist.
- `answers.md`
    - Contains the answers to the 6 questions asked at the end of the assignment. I put them in a `.md` file instead of
      a `.txt` for better readability.
- `cvals.csv`
    - The exported csv, with all the containment values for each pair of files.
- `main.py`
    - The main python file that is used to run the project.
- `requirements.txt`
    - Contains the required pip packages needed to run the project.

### Running the Project

> 1. Ensure you are in the root directory of the project.
> 2. Run `pip install -r requirements.txt` to install the required packages.
> 3. Run `python main.py` to run the project to determine the containment values for each pair of files. All outputs and locations are specified in the above section.