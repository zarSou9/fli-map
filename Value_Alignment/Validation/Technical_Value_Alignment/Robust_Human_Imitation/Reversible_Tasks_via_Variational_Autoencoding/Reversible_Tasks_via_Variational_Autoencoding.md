### Mini Description

Using deep generative models to learn tasks that can be undone

### Description

For the subset of human tasks that are reversible, or able to be done either forwards or backwards with minimal information loss, one can form generative models based on training data of queries and associated good responses ([Taylor et al. 2016](https://intelligence.org/files/AlignmentMachineLearning.pdf)). Variational autoencoders seem appropriate for this as they learn lower-dimensional manifolds that tease out conceptual structure (Kingma and Welling 2013). It might also be possible to break such nonreversible tasks into multiple reversible tasks to leverage this technique ([Stuhlm"uller et al. 2013](http://papers.nips.cc/paper/4966-learning-stochastic-inverses.pdf)). Just which sets of tasks can be performed using reversible generative models remains underexplored.
