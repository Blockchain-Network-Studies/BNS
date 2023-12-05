# Blockchain Network Studies

*This repository contains the replicable data and code for research entitled "Is decentralized finance actually decentralized? A social network analysis of the Aave protocol on the Ethereum blockchain."*

<blockquote style="color: green;">
   <strong>Innovation and Inclusivity Statements</strong>:
   In line with the web3 ethos, this study provides open-source data and code, ensuring transparency and facilitating replicability. These resources are available at our GitHub repository, underscoring our commitment to decentralized, community-driven research practices. Our Python code in Jupyter Notebook can be run on both the cloud computing platform Google Colab and locally. We are dedicated to promoting diversity and inclusion, not only as research advocates but also in our own research practices.</p>
</blockquote>

<blockquote style="color: green;">
   <strong>Abstract</strong>
   Decentralized finance (DeFi) has the potential to disrupt centralized finance by validating peer-to-peer transactions through tamper-proof smart contracts, thus significantly lowering the transaction cost charged by financial intermediaries. However, the actual realization of peer-to-peer transactions and the levels and effects of decentralization are largely unknown. Our research pioneers a blockchain network study that applies social network analysis to measure the level, dynamics, and impacts of decentralization in DeFi token transactions on the Ethereum blockchain. First, we find a significant core-periphery structure in the AAVE token transaction network where the cores include the two largest centralized crypto exchanges. Second, we provide evidence that multiple network features consistently characterize decentralization dynamics. Finally, we document that a more decentralized network significantly predicts a higher return and lower volatility of the decentralized market of AAVE tokens on the Ethereum blockchain. We point out that our approach is seminal for inspiring future extensions related to the facets of application scenarios, research questions, and methodologies on the mechanics of blockchain decentralization. 
   
  <strong>Keywords</strong>: Decentralized finance, social network analysis, AAVE, Ethereum, core-periphery, modularity, giant component ratio
  
  <strong>ACM CCS</strong>: E.0, G.1, G.3,  I.6, J.4, J.6
  
  <strong>JEL Code</strong>: C15, C22, C23, C58, C63, C81, G17
  
</blockquote>

## Table of Contents:

- [Code](https://github.com/Blockchain-Network-Studies/BNS/tree/main/Code)
    - Jupyter Notebooks for data analysis
    - Scripts for data processing and visualization
- [Data](https://github.com/Blockchain-Network-Studies/BNS/tree/main/Data)
    - Raw data sets used in the study
    - Processed data files

- [Appendix](https://github.com/Blockchain-Network-Studies/BNS/tree/main/Appendix)
    - Additional analyses
    - Supplementary data interpretations

## Notes on updating large data files:

- Install Git LFS by running
```
git lfs install
```
- Track large files with 

```
git lfs track "*.csv"
```
- Commit and push as usual. The large files will be managed by Git LFS.
