#!/bin/bash
#command line for spmf mining

# minsup: 40%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_40.txt 0.40

# minsup: 45%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_45.txt 0.45

# minsup: 50%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_50.txt 0.50

# minsup: 55%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_55.txt 0.55

# minsup: 60%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_60.txt 0.60

# minsup: 65%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_65.txt 0.65

# minsup: 70%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_70.txt 0.70

# minsup: 75%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_75.txt 0.75

# minsup: 80%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_80.txt 0.80

# minsup: 85%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_85.txt 0.85

# minsup: 90%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encoded_for_SPMF.txt output_90.txt 0.90
