# MastersDissertationProject
This repository is all code used to produce Joseph Findlays masters dissertation. 
It should be noted that any methods used have been cited in the original dissertation itself. 
Code has been reused, and normally repurposed and edited in certain places from various sources, including the TIA lab itself as well as the computational biology module at Warwick University. 
### File Contents 
#### AllNotebooks
- In this section we have the main body of notebooks used, it should be noted that these jupyter notebooks used google colab, hence the installs at the start of each notebook.
- It should be noted that directorys have either been removed for privacy purposes, or are for not included due to the amount storage neccessary to store Whole Slide Images. The original public WSSS4LUAD training data can be found at :
https://drive.google.com/drive/folders/1qTTTaHAp8HOnvxnKi1RXp-bC7sito9DF
- Notebooks in certain areas should not be run sequentially, and are mainly for evalution purposes rather than to be reused. 

- PatchClassificationLUAD.ipynb shows all code for the patch classification section.
- CAMMaskproduction.ipynb is the code used to create masks from class activation maps. 
- Both SegmentationDeepLabV3Plus.ipynb and SegmentationLUAD.ipynb are both pytorch files that include code for the segmentation task.
- GRID_Model_implementation.ipynb is the code used for the original GRID model implementation.
- Grid_seg_Tumour_nonTumour.ipynb is a full notebook showcasing the production and 
- UHCWRoiPrediction.ipynb is for external dataset ROI segementation. 


#### ROICode
This folders provides the python files used to get_rois, stain normalise and segment them. 
