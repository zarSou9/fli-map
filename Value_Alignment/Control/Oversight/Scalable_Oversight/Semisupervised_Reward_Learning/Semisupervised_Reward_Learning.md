### Mini Description

Train a semisupervised model to predict the reward for given unlabelled scenarios based on a much smaller set of labelled scenarios, and use that model in turn to train the agent

### Description

A somewhat scalable approach is to train a reinforcement learning model in a semi-supervised manner ([Finn et al. 2016](https://arxiv.org/pdf/1612.00429v1)) to predict the reward from the state on either a per-timestep or per-episode basis, and use it to estimate the payoff ([Amodei et al. 2016](http://arxiv.org/abs/1606.06565)) of unlabelled episodes, with some appropriate weighting or uncertainty estimate to account for lower confidence in estimated vs known reward ([Daniel et al. 2015](http://www.ausy.tu-darmstadt.de/uploads/Team/ChristianDaniel/ActiveRewardLearning.pdf)).
