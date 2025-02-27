### Mini Description

Applying end-to-end verification techniques to whole AI systems

### Description

The verification of whole AI systems has been underexplored, but a number of challenges are clear. A number of principles to address these challenges have been proposed ([Seshia et al. 2016](https://people.eecs.berkeley.edu/~dsadigh/Papers/seshia-verifiedAI-arxiv.pdf)): introspective environment modeling, end-to-end specifications and specification mining, developing abstractions for and explanations from ML components, creating new randomized formal methods for systematically generating realistic data, and developing verification engines more oriented around run time, quantitative operations, and learning ([Seshia et al. 2016](https://people.eecs.berkeley.edu/~dsadigh/Papers/seshia-verifiedAI-arxiv.pdf)). A number of challenges to verifying AI systems in the general case remain ([Yampolskiy 2016](https://arxiv.org/pdf/1609.00331v3)). Following a componentized architecture, in which guarantees about individual components can be combined according to their connections to yield properties of the overall system seems promising ([Seshia et al. 2016](https://people.eecs.berkeley.edu/~dsadigh/Papers/seshia-verifiedAI-arxiv.pdf)). Review and remediation of systemic issues such as questionable data dependencies, unpleasantly unexpected data flow dynamics, inappropriate or suboptimal abstractions, and mixed technology stacks ([Sculley et al. 2014](http://research.google.com/pubs/archive/43146.pdf)) will help to simplify AI systems to help make them more likely to be meaningfully verifiable.

### Related Nodes

- [ML with Contracts](/Value_Alignment/Validation/Increasing_Contextual_Awareness/Uncertainty_Identification_and_Management/Inductive_Ambiguity_Identification/Robustness_to_Distributional_Shift/ML_with_Contracts/ML_with_Contracts.md)
	- Reason: From Verification of Whole AI Systems also see ML with Contracts as software interface contracts make segmentations within the analyses needed for formal verification much easier.
