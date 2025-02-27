### Mini Description

Non-bayesian techniques that allow learners to calibrate their confidence in their predictions

### Description

Most machine learning methods do not by default identify ambiguities well, either lacking such a concept entirely, or often poorly calibrated at doing so even if overall accuracy is high ([Taylor et al. 2016](https://intelligence.org/files/AlignmentMachineLearning.pdf)). It is well known that neural networks are often overconfident in their results, but there has been recent work to calibrate their confidences better ([Goodfellow et al. 2015](https://pdfs.semanticscholar.org/bee0/44c8e8903fb67523c1f8c105ab4718600cdb.pdf), [Nguyen et al. 2015](http://yosinski.com/media/papers/Nguyen__2015__CVPR__Deep_Neural_Networks_Are_Easily_Fooled.pdf)). The techniques of conformal prediction attempt to produce well-calibrated sets of possible predictions ([Vovk et al. 2005](http://www.alrw.net/)).
