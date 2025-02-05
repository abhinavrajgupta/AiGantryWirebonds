<div align="center">
  <h1>Wirebonds Detection on Silicon Modules</h1>
  <p>Welcome to the Wirebonds Detection on Silicon Modules repository! This project is designed to perform wirebond inference on images captured from OGP machine and generate insightful data analysis through detailed histograms and summary reports.</p>
</div>

---

## Getting Started

### Prerequisites
Please note that setting up a new Conda environment is required to run these scripts. The Conda environment configuration is provided in the **environment.yml** file. Additionally, please ensure you have an **Ubuntu Linux System** to run this program; otherwise, you might encounter numerous PackageNotFound errors.

### Installation
#### Clone the repository and set up the environment:
     git clone https://github.com/abhinavrajgupta/AiGantryWirebonds
     cd AiGantryWirebonds
     conda env create -f environment.yml
     conda activate Wirebond

### Adding Modules and Imgaes
The code in this repository is structured to specify paths for uploading images. Ensure that you place your upload module in the appropriate directory to maintain compatibility with the codebase. The path format follows this structure: 
######  current_directory/Modules/(Upload_Module_Here)
        mkdir Modules
#### Upload your Images here
##### [For Example you will upload M15 in the Modules file such that the path is structured as Modules/M15/(images and text file here)]

## How It Works
### 1. Upload Images:
  - Place your OGP-captured images in the specified directory.
### 2. Run Wirebond Detection:
  - Execute the detection script to infer wirebond characteristics from the images.
### 3. Data Analysis:
  - Run the analysis script to generate histograms and a comprehensive summary table of the inference results.

## Usage:
### 1. Run Detection Script:
     python wirebonddetect.py
### 2. Generate Analysis:
###### Before running this script, please open **analyze_results.py** and update your current directory as base directory in the first function.
     python analyze_results.py

## Results:
### 1. Detection Results: Images with labels saved at:
    ../Modules/Module_Name/Reuslts
### 2. Histogram: Visual representation of key detection metrics saved at:
    ../Modules/Module_Name/Reuslts/Histogram.jpg
### 3. Summary Table: Comprehensive insights into wirebond detection results saved at:
    ../Modules/Module_Name/Reuslts/Summary_Table.csv

## Contributing
#### Contributions are welcome! Feel free to fork the repository and submit pull requests.










<br><br><br> <!-- This will create a gap -->
<br><br><br> <!-- This will create a gap -->





