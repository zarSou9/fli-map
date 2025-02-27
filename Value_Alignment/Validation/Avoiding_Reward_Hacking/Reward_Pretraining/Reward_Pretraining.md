### Mini Description

Training the reward function in a supervised manner offline, ahead of online use

### Description

Another way to discourage gaming of the reward function is to train the reward function in a supervised manner offline, ahead of online use ([Amodei et al. 2016](http://arxiv.org/abs/1606.06565), [Finn et al. 2016a](http://jmlr.org/proceedings/papers/v48/finn16.pdf)). As a known function, it can be analyzed analytically, statically, or in unit tests, and it will by definition be robust against online reward function corruption.
