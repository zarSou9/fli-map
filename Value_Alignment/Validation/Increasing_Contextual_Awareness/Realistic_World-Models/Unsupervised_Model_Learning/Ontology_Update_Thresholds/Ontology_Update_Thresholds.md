### Mini Description

Thresholds or frequency of world models updates should be tuned to prevent suffering from serious instances of concept drift

### Description

Ontology rot occurs when one or more concepts in a world model are held fixed as new dynamics emerge which merit updates to the world model (Zablith 2009, [Mallah 2015](http://smartdata2015.dataversity.net/sessionPop.cfm?confid=91&proposalid=7754), [Noy and Klein 2004](https://pdfs.semanticscholar.org/e38f/9d0878d9b06713142331695efe9ce5e5e0e0.pdf)). When a measure or property becomes a target or a key performance indicator, the dynamics of the system change to optimize for it, often in unexpected or parochial ways, causing that metric to no longer be a good measure (Mallah 2017). This is known as Goodhart's Law ([Manheim 2016](http://www.ribbonfarm.com/2016/06/09/goodharts-law-and-why-measurement-is-hard/)). Insufficiently adaptive ontologies can lead to parochial behaviors with justifications that may no longer be grounded (Zablith 2009, [Noy and Klein 2004](https://pdfs.semanticscholar.org/e38f/9d0878d9b06713142331695efe9ce5e5e0e0.pdf)). Ontologies updated too frequently or with too little evidence, however, can lead to mercurial behavior ([Mallah 2014](https://people.eecs.berkeley.edu/~russell/research/future/mallah-aamas14-future.pdf)).

### Related Nodes

- [Avoiding Reward Hacking](/Value_Alignment/Validation/Avoiding_Reward_Hacking/Avoiding_Reward_Hacking.md)
- [Degree of Value Evolution](/Value_Alignment/Validation/Technical_Value_Alignment/Degree_of_Value_Evolution/Degree_of_Value_Evolution.md)
	- Reason: From Ontology Update Thresholds also see Degree of Value Evolution since, relatedly, when a property degrades in its role as a moral value, reevaluation of the intent of that value may be necessary.
- [Mild Optimization](/Value_Alignment/Validation/Averting_Instrumental_Incentives/Domesticity/Mild_Optimization/Mild_Optimization.md)
	- Reason: From Ontology Update Thresholds also see Mild Optimization because developing a formal model of Goodharts Law can also benefit that need.
