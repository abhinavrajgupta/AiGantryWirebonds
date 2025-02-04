# Wirebonds Detection on Silicon Modules

### Welcome to the Wirebonds Detection on Silicon Modules repository! This project is designed to perform wirebond inference on images captured from OGP machine and generate insightful data analysis through detailed histograms and summary reports.

## Getting Started

### Prerequisites
Please note that setting up a new Conda environment is required to run these scripts. The Conda environment configuration is provided in the **environment.yml** file. Additionally, please ensure you have an **Ubuntu Linux System** to run this program; otherwise, you might encounter numerous PackageNotFound errors.

### Installation
#### Clone the repository and set up the environment:
     git clone https://github.com/AiGantryWirebonds.git
     cd AiGantryWirebonds
     conda env create -f environment.yml

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
  - python wirebonddetect.py
### 2. Generate Analysis:  
  - python analyze_results.py

## Results:
### 1. Detection Results: Images with labels saved at:
    Modules/Module_Name/Reuslts
### 2. Histogram: Visual representation of key detection metrics saved at:
    AiGantryWirebonds/Modules/Module_Name/Reuslts/Histogram.jpg
### 3. Summary Table: Comprehensive insights into wirebond detection results saved at:
    AiGantryWirebonds/Modules/Module_Name/Reuslts/Summary_Table.csv

## Contributing
#### Contributions are welcome! Feel free to fork the repository and submit pull requests.










<br><br><br> <!-- This will create a gap -->
<br><br><br> <!-- This will create a gap -->





<div align="center">
<p>
<a align="left" href="https://ultralytics.com/yolov5" target="_blank">
<img width="850" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/splash.jpg"></a>
</p>
<br>
<div>
<a href="https://github.com/ultralytics/yolov5/actions"><img src="https://github.com/ultralytics/yolov5/workflows/CI%20CPU%20testing/badge.svg" alt="CI CPU testing"></a>
<a href="https://zenodo.org/badge/latestdoi/264818686"><img src="https://zenodo.org/badge/264818686.svg" alt="YOLOv5 Citation"></a>
<br>  
<a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
<a href="https://www.kaggle.com/ultralytics/yolov5"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>
<a href="https://hub.docker.com/r/ultralytics/yolov5"><img src="https://img.shields.io/docker/pulls/ultralytics/yolov5?logo=docker" alt="Docker Pulls"></a>
</div>
  <br>
  <div align="center">
    <a href="https://github.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://www.linkedin.com/company/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-linkedin.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://twitter.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-twitter.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://youtube.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-youtube.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://www.facebook.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-facebook.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://www.instagram.com/ultralytics/">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-instagram.png" width="2%"/>
    </a>
</div>

