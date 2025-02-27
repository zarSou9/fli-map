### Mini Description

Structuring learning to be robust to when adversaries pick test data from different distributions than training data

### Description

An agent is more robust when one can guarantee its good behavior even when an adversary picks test or production data for it, from a different distribution than training data, aiming to make the agent fail ([Taylor et al. 2016](https://intelligence.org/files/AlignmentMachineLearning.pdf)). It is increasingly common that machine learning systems can be manipulated ([Papernot et al. 2016](http://arxiv.org/abs/1602.02697), [Goodfellow et al. 2015](https://pdfs.semanticscholar.org/bee0/44c8e8903fb67523c1f8c105ab4718600cdb.pdf), [Moosavi-Dezfooli et al. 2016](http://arxiv.org/abs/1610.08401)), and this can even happen with real-world examples ([Kurakin et al. 2016](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45471.pdf)).

### Related Nodes

- [Counterexample Resistance](/Value_Alignment/Validation/Avoiding_Reward_Hacking/Counterexample_Resistance/Counterexample_Resistance.md)
	- Reason: From Adversarial ML also see Counterexample Resistance as this issue is core to concept learning and validation as well.
- [Inductive Ambiguity Identification](/Value_Alignment/Validation/Increasing_Contextual_Awareness/Uncertainty_Identification_and_Management/Inductive_Ambiguity_Identification/Inductive_Ambiguity_Identification.md)
	- Reason: From Adversarial ML also see Inductive Ambiguity Identification since dynamics-induced ambiguity issues and adversarially-introduced ones share many features, and many of the techniques that help with the former will also help with the latter.
- [Adversarial Transparency](/Value_Alignment/Control/Oversight/Monitoring/Adversarial_Transparency/Adversarial_Transparency.md)
