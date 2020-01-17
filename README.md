## UE901 Data Mining Practical Project - Itemset and Association Rules Mining on GrandEst data
**IDMC M2 NLP Yi-Ting TSAI & Sophea LY**

This is a repository containing all the necessary files for the project of the class UE901 Data Mining with Professor Mr. Yannick Toussaint, beneath you can find basic description of this repository, as well as the instructions and snippets for running the encoder and decoder scripts. 

### About this repository
Files, repos, etc

### Starting
Please clone this repository with the code here:

```bash
git clone git@github.com:yiting-tsai/data-mining-practical.git
```

### Wrangling the data for SPMF
** Make sure you have the encoder script ```Encoder4SPMF.py``` and ```GrandEst.csv``` in the same directory as .

In terminal of the folder of encoder script and dataset, 
```bash
python Encoder4SPMF.py GrandEst.csv
```
and the output of the encoder program is ```GrandEst_encoded_for_SPMF.txt```.

### Mining with SPMF
At the same directory, have your ```spmf.jar``` ready inside and in the terminal,
```bash
SPMF_commandline.sh
```
it'll output the results along with the corresponding *min_sup* value. 
For example, an output of the *min_sup=0.6* would be ```output_60.txt```. 

### Decoding the SPMF format
The snippet below will give the decoded file back, so in terminal:
```bash
python DecodeAfterSPMF.py output_60.txt
```
### Association rules mining

