### Mini Description

An approach for satisficing expected reward rather than using an extreme solution to maximize it

### Description

Rather than seeking the most extreme solution to a problem, i.e. maximizing a function such as expected reward, one can instead seek to satisfice expected reward ([Simon 1956](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.545.5116&rep=rep1&type=pdf), [Taylor et al. 2016](https://intelligence.org/files/AlignmentMachineLearning.pdf)). This may be approached by choosing actions from a top percentage of possible actions per a sort by expected reward or probability of success though that alone wouldn't necessarily prevent satisfaction from overoptimization ([Taylor 2016](https://intelligence.org/files/QuantilizersSaferAlternative.pdf)). The technique of quantilization selects a strategy randomly within some top percentile of strategies ([Taylor 2016](https://intelligence.org/files/QuantilizersSaferAlternative.pdf)), which probabilistically mitigates such risk.

### Related Nodes

- [Logical Counterfactuals](/Value_Alignment/Foundations/Consistent_Decision_Making/Decision_Theory/Logical_Counterfactuals/Logical_Counterfactuals.md)
	- Reason: From Quantilization also see Logical Counterfactuals as that can assist with enumeration of options.
