# Introduce
This directory contains experimental data and experimental scripts related to Exp3.

- **the_weight_of_relevance_is_0** is the reuslt of `B-TIPS` when relevance is not considered and only plan differences is considered.
- **the_weight_of_relevance_is_0.5** is the reuslt of `B-TIPS` when both relevance and plan differences are considered.
- **the_weight_of_relevance_is_1** is the reuslt of `B-TIPS` when plan differences is not considered and only relevance is considered.
- **sql** contains the sql statement used in this experiment.

# Conduct Experiment
This experiment involves only one function `INFOPLAN_TIPS`. You just need to adjust the value of the global variable `gLambda` to get the results in different situations. A simpler method is to adjust the control parameter `lambda` of the front end, and you can also get the results with different weights of relevance and plan difference. 

Note that `lambda` is the weight of plan differences. So if you want the result of **the_weight_of_relevance_is_0** you need to set `lambda` to 1.