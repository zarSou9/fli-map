### Mini Description

Training a highly capable aligned agent using a succession of approval-directed agents

### Description

Generally, one can consider the combination of multiple learning and validation techniques for learning what a human would respond, or how they would judge a situation, reserving active learning and querying of humans for when it's quite necessary ([Christiano 2015e](https://medium.com/ai-control/mimicry-maximization-and-meeting-halfway-c149dd23fc17)). It has also been proposed that one might train a highly capable aligned agent using a mix of a series of more capable approval-directed reinforcement learning agents and bootstrapping ([Christiano 2016](https://medium.com/ai-control/alba-an-explicit-proposal-for-aligned-ai-17a55f60bbcf)). In theory, it would be possible to establish a trajectory whereby the succession becomes capable of closely approximating what the human would have decided given much more time, resurces, and education. This is, however, much more difficult than developing a good generative model of observed human behavior.

### Related Nodes

- [Human Judgement Learner](/Value_Alignment/Control/Oversight/Scalable_Oversight/Human_Judgement_Learner/Human_Judgement_Learner.md)
	- Reason: From Scaling Judgement Learning also see Human Judgement Learner where a similar technique is used in a continuous online manner.
- [Scalable Oversight](/Value_Alignment/Control/Oversight/Scalable_Oversight/Scalable_Oversight.md)
