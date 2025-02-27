### Mini Description

Train a model to predict the reward for given unlabelled scenarios based on a set of labelled scenarios, and use that model to train the agent

### Description

With a supervised reward learning approach, one can train a model to predict the reward from the state on either a per-timestep or per-episode basis, and use it to estimate the payoff of unlabelled episodes ([Amodei et al. 2016](http://arxiv.org/abs/1606.06565)), with some appropriate weighting or uncertainty estimate to account for lower confidence in estimated versus known reward ([Daniel et al. 2015](http://www.ausy.tu-darmstadt.de/uploads/Team/ChristianDaniel/ActiveRewardLearning.pdf), [Schulman et al. 2016](https://arxiv.org/pdf/1506.02438.pdf)).
