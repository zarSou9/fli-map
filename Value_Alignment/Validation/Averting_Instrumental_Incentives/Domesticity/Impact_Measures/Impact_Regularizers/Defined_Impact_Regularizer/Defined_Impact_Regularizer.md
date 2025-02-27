### Mini Description

Methods for penalizing an agent for recognizably changing the world as per particular given measures

### Description

If one has enough of an object-level understanding of what the agent will encounter in advance, one can elect particular impact measures to use in the regularizers that temper impact. One can choose to penalize changing the environment overall ([Amodei et al. 2016](http://arxiv.org/abs/1606.06565), [Taylor et al. 2016](https://intelligence.org/files/AlignmentMachineLearning.pdf)) or one can introduce a penalty for changes relative to some baseline environmental state or a baseline policy determined by some explicit method ([Armstrong and Levinstein 2015](https://dl.dropboxusercontent.com/u/23843264/Permanent/Reduced_impact_S+B.pdf)). One can start from safe policy and try to improve the policy it from there, in manners similar to reachability analysis ([Lygeros et al. 1999](http://dx.doi.org/10.1016/S0005-1098(98)00193-9), [Mitchell et al. 2005](https://www.cs.ubc.ca/~mitchell/Papers/publishedIEEEtac05.pdf)) or to robust policy improvement ([Iyengar 2005](http://dx.doi.org/10.1287/moor.1040.0129), [Amodei et al. 2016](http://arxiv.org/abs/1606.06565), [Nilim and Ghaoui 2005](http://dx.doi.org/10.1287/opre.1050.0216)).

### Related Nodes

- [Verification of Machine Learning Components](/Value_Alignment/Verification/Verification_of_Intelligent_Systems/Verification_of_Machine_Learning_Components/Verification_of_Machine_Learning_Components.md)
- [Penalize Influence](/Value_Alignment/Validation/Averting_Instrumental_Incentives/Domesticity/Impact_Measures/Avoiding_Negative_Side_Effects/Penalize_Influence/Penalize_Influence.md)
