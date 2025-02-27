### Mini Description

Train a model to identify relevant features for determining reward, and having it query human operators about rewards judiciously

### Description

With active reward learning, one trains a model in an active learning manner to predict the reward from the state on either a per-timestep or per-episode basis, and use it to estimate the payoff of unlabelled episodes ([Daniel et al. 2015](http://www.ausy.tu-darmstadt.de/uploads/Team/ChristianDaniel/ActiveRewardLearning.pdf)), e.g. identifying salient events in the environment and querying human operators as to the respective rewards ([Amodei et al. 2016](http://arxiv.org/abs/1606.06565)).
