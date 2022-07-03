# Are decentralized finance really decentralized? A social network analysis of the Aave protocol on the Ethereum blockchain
**Check out the Paper on arXiv**: [arxiv.org/abs/2205.04256](https://arxiv.org/abs/2205.04256)

## *Supplementary resources, data, and code*

**by Ziqiao Ao<sup>#</sup>, and Gergely Horvath\*, Luyao Zhang\***, 

\*: joint corresponding authors

\#: undergraduate advisee and mentee

*names by the alphabetical order of the last names*

![image](https://github.com/Blockchain-Network-Studies/BNS/blob/main/Figures/Contribution_map.png)

|   **Folder**   | **URL** | 
|:------------|:---------|
|   Data  | https://github.com/Blockchain-Network-Studies/BNS/tree/main/Data|   
|  Figure| https://github.com/Blockchain-Network-Studies/BNS/tree/main/Figures |  
|  Core-peripheral Analysis |  https://github.com/Blockchain-Network-Studies/BNS/tree/main/Core-peripheral_Analysis |  
|Network Features|https://github.com/Blockchain-Network-Studies/BNS/tree/main/Network_Features | 
|Regressions| https://github.com/Blockchain-Network-Studies/BNS/tree/main/Regressions| 
|Invitation letter| https://github.com/Blockchain-Network-Studies/BNS/tree/main/invitation_letters|                                                                      

# The Collection of Datasets
## Data Overview

|   **Name**   | **Description** |  **URL** | 
|:---|:----------------|:------|
|   AAVE Raw Transfer   |  The Aave token raw transfer data records every transaction with Aave, including the address of the sender, and receiver, the transaction timestamp in each block and the transaction value.  | https://github.com/Blockchain-Network-Studies/BNS/blob/main/Data/Aave_Raw_Transfer_Data.csv|   
|   AAVE Transfer after Preprocessing  |  Deviated from the raw transfer data, after converting timestamp to date and dropping all the transaction records that contain null addresses, the transaction values between the same two addresses are added together to one aggregated transaction by date. This dataset could be directly used for network feature calculation.| https://github.com/Blockchain-Network-Studies/BNS/blob/main/Data/AAVE_transaction_data_after_preprocessing.csv |  
|   Network Features  |  This dataset contains 23 daily network topological features calculated from the Aave transaction data. | https://github.com/Blockchain-Network-Studies/BNS/blob/main/Data/AAVE_Network_Features.csv |  
|  Merged Dataset  |The final dataset contains all the DeFi token-related economic features and network features, which could be directly used for quantitative analysis|https://github.com/Blockchain-Network-Studies/BNS/blob/main/Data/AAVE_Merged_Datasets.csv |  
|  Core Addresses Appearance  |This dataset records all core addresses that appear at the selected time period and the number of days they become core, based on the daily networks constructed using a core-periphery algorithm. The type and information link of the addresses are contained as well.| https://github.com/Blockchain-Network-Studies/BNS/blob/main/Data/core_addresses_appearance.csv | 


# The Collection of Colab Notebooks

|   **Notebook**   | **URL** | 
|:------------|:---------|
|   Notebook 1: Network and Core-periphery Analysis  | [https://github.com/Blockchain-Network-Studies/BNS/tree/main/Data](https://github.com/Blockchain-Network-Studies/BNS/blob/main/Network_Features/Notebook_1__network_core_periphery_analysis.ipynb)|   
|  Notebook 2: Generate Merged Dataset| [https://github.com/Blockchain-Network-Studies/BNS/tree/main/Figures](https://github.com/Blockchain-Network-Studies/BNS/blob/main/Regressions/Notebook_2_Generate_Merged_Dataset.ipynb) |  
|  Notebook 2: Visualization, Data Science and Economics Analysis|  [https://github.com/Blockchain-Network-Studies/BNS/tree/main/Core-peripheral_Analysis](https://github.com/Blockchain-Network-Studies/BNS/blob/main/Regressions/Notebook_3_Analysis.ipynb) |                                                       

# Presentations

Slides for 29th Annual Global Finance Conference Presentation

Braga, Portugal ​

Date: 6/21/2022

https://github.com/Blockchain-Network-Studies/BNS/blob/main/invitation_letters/BNS_Slides.pdf
