### Mini Description

Preventing an agent from gaming its reward function

### Description

A very intelligent agent built to optimize just its observations rather than some function in the actual environment would likely not align with human interests ([Bostrom 2014](https://global.oup.com/academic/product/superintelligence-9780199678112)). It may very well cause unanticipated and potentially harmful behavior by gaming its reward function, deluding itself whether purposefully or inadvertantly ([Thompson 1997](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.26.6187&rep=rep1&type=pdf), [Bird and Layzell 2002](https://people.duke.edu/~ng46/topics/evolved-radio.pdf)). Determining how one can reliably prevent an agent from gaming its reward function like this is an open area of research, thus far with a number of promising ideas for mitigation ([Dewey 2011](http://www.danieldewey.net/learning-what-to-value.pdf), [Orseau and Ring 2011](http://dx.doi.org/10.1007/978-3-642-22887-2_1), [Amodei et al. 2016](http://arxiv.org/abs/1606.06565)).

### Related Nodes

- [Theory of Counterfactuals](/Value_Alignment/Foundations/Foundations_of_Rational_Agency/Theory_of_Counterfactuals/Theory_of_Counterfactuals.md)
- [Goal Stability](/Value_Alignment/Foundations/Consistent_Decision_Making/Goal_Stability/Goal_Stability.md)
- [Tripwires](/Value_Alignment/Security/Tripwires/Tripwires.md)
	- Reason: From Avoiding Reward Hacking also see Tripwires which may be used to help catch these behaviors.
- [Ontology Update Thresholds](/Value_Alignment/Validation/Increasing_Contextual_Awareness/Realistic_World-Models/Unsupervised_Model_Learning/Ontology_Update_Thresholds/Ontology_Update_Thresholds.md)
	- Reason: From Avoiding Reward Hacking also see Ontology Update Thresholds as the dynamic degradatory repurposing of properties as in Goodhart's Law surfaces in both.
