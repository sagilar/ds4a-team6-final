# ds4a-team6 MINJUSTICIA
## Correlation One - MINTIC

This repository contains all the code about the developments of the project carried out for MINJUSTICIA, implemented by Team 6.  

It is composed of several jupyter notebooks which have the corresponding analysis of the EDA. Each one has a preffix according to the specific analysis.  

The dashboard application is within the `dash_template_minjusticia` folder; inside this folder all the components required to run the application are there.  Run it by running `python3 index.py`.  

The models that were developed during the project have their specific jupyter notebook with their corresponding descriptions. They are named with the MODELS preffix. Additionally, the embedded models (pickle files) are already in the Dash application.  

The `retomintic` folder contains the data provided by MINJUSTICIA.  

Finally, the `Ds4At6.Api` contains the code related to the implemented APIs for querying and extracting the data directly from Azure.

Please install the required modules by running `pip3 install -r requirements.txt`
