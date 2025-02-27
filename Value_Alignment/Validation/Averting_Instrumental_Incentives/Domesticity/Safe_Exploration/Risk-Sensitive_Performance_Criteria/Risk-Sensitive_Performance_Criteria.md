### Mini Description

Changing optimization criteria from total expected reward to other objectives that prevent or minimize downsides of note

### Description

One can change optimization criteria from just total expected reward to other objectives that prevent or minimize downsides of note ([Garcia and Fernandez 2015](http://www.jmlr.org/papers/volume16/garcia15a/garcia15a.pdf), [Tamar et al. 2014](http://arxiv.org/abs/1404.3862), [Amodei et al. 2016](http://arxiv.org/abs/1606.06565), [Thomas et al. 2015](http://psthomas.com/papers/Thomas2015.pdf)). It's also possible to estimate uncertainty within value functions, which could be incorporated into risk-sensitive reinforcement learning ([Osband et al. 2016](http://papers.nips.cc/paper/6500-deep-exploration-via-bootstrapped-dqn.pdf), [Gal and Ghahramani 2016](http://jmlr.org/proceedings/papers/v48/gal16-supp.pdf)), which may also model "intrinsic fear" with probabilities on how close in steps different states are to catastrophe ([Lipton et al. 2016](https://arxiv.org/pdf/1611.01211v3)).
