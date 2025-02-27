### Mini Description

A technique where successively better reinforcement learners bootstrap off of each other and supplement learning with active learning

### Description

Techniques for learning human judgement are another approach to scalable control ([Taylor et al. 2016](https://intelligence.org/files/AlignmentMachineLearning.pdf)). While some are less scalable or more narrow ([Knox and Stone 2009](http://www.cs.utexas.edu/~pstone/Papers/bib2html-links/KCAP09-knox.pdf)), others aim to be highly scalable ([Christiano 2014c](https://medium.com/ai-control/model-free-decisions-6e6609f5d99e)). In the latter case, one might train a reinforcement learning system to take actions that a human would rate highly by using a framework where the system has to learn the human judgment reward function, and where training data is produced by having a more advanced agent, e.g. a human, evaluate the learners actions ([Christiano 2015e](https://medium.com/ai-control/mimicry-maximization-and-meeting-halfway-c149dd23fc17)), approval-directed agents ([Christiano 2016](https://medium.com/ai-control/alba-an-explicit-proposal-for-aligned-ai-17a55f60bbcf)).

In ambitious conceptions of this, the goal is not just to form a good generative model of observed human judgement, but the much more difficult goal of using the trajectories of past learning to extrapolate forward to what the subject would decide given more time, education, and resources.

### Related Nodes

- [Scaling Judgement Learning](/Value_Alignment/Validation/Technical_Value_Alignment/Robust_Human_Imitation/Scaling_Judgement_Learning/Scaling_Judgement_Learning.md)
	- Reason: From Human Judgement Learner also see Scaling Judgement Learning where a comparable technique is used for upfront value learning.
- [Inverse Reinforcement Learning](/Value_Alignment/Validation/Technical_Value_Alignment/Robust_Human_Imitation/Inverse_Reinforcement_Learning/Inverse_Reinforcement_Learning.md)
	- Reason: From Human Judgement Learner also see Inverse Reinforcement Learning a practicable technique for apprenticeship learning and determining human goals.
