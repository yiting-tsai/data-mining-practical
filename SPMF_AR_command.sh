#!/bin/bash
#command line for spmf association rules mining

# minsup 80% minconf 60%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encoded_for_SPMF.txt output_sup80_conf60.txt 80% 60%

# minsup 80% minconf 80%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encoded_for_SPMF.txt output_sup80_conf80.txt 80% 80%

# minsup 85% minconf 85%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encoded_for_SPMF.txt output_sup85_conf85.txt 85% 85%


