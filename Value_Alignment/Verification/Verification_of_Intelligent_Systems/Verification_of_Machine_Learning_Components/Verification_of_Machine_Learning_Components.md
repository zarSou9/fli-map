### Mini Description

Applying verification to components or algorithms that learn from data

### Description

Each type of machine learning algorithm or paradigm may need to be considered individually with respect to what aspects need better formalization, quantization, introspection, or proofs ([Russell et al. 2015](http://futureoflife.org/data/documents/research_priorities.pdf)). There has been some work on requirements for verifying neural networks ([Pulina and Tacchella 2010](https://pdfs.semanticscholar.org/72e5/5b90b5b791646266b0da8f6528d99aa96be5.pdf), [Schumann and Liu 2010](http://www.springer.com/gp/book/9783642106897)). There has also been exploration of directions for more nuanced and efficient summarization of the high-dimensional distributions many learning algorithms produce ([Achim et al. 2016](http://www.jmlr.org/proceedings/papers/v48/achim16.pdf), null, [Kim et al. 2016](https://cs.stanford.edu/~ermon/papers/kim-sabharwal-ermon.pdf)), whereby quantization of the distributions might enable simple deductive proofs and satisfiability analyses. State coarse-graining or abstraction for reinforcement learners conforming to specified partial programs provide a path for formalized treatment of learned policies ([Andre and Russell 2002](https://people.eecs.berkeley.edu/~russell/papers/aaai02-alisp.pdf)). In addition to accounting for particular learned models, one must also account for future changes to the learner as new data arrives, another underexplored challenge ([Seshia et al. 2016](https://people.eecs.berkeley.edu/~dsadigh/Papers/seshia-verifiedAI-arxiv.pdf)).

### Related Nodes

- [Defined Impact Regularizer](/Value_Alignment/Validation/Averting_Instrumental_Incentives/Domesticity/Impact_Measures/Impact_Regularizers/Defined_Impact_Regularizer/Defined_Impact_Regularizer.md)
	- Reason: From Verification of Machine Learning Components also see Defined Impact Regularizer as there are conceptual parallels between partial programs and distance from a baseline policy.
