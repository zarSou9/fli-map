### Mini Description

Establishing the bounds inside of which mistakes are recoverable and exploring only within that area

### Description

Another way to explore safely is to model or otherwise determine the state space regions in which mistakes are relatively inconsequential or recoverable, and exploring only within those areas ([Moldovan and Abbeel 2012](http://icml.cc/2012/papers/838.pdf), [Amodei et al. 2016](http://arxiv.org/abs/1606.06565)). Recent techniques that do this iteratively for safe exploration using markov decision processes ([Turchetta et al. 2016](http://arxiv.org/abs/1606.04753)) and gaussian processes ([Schreiter et al. 2015](http://www.jmlr.org/proceedings/papers/v37/sui15.pdf)) can explore unknown environments without getting into irreversible situations.

### Related Nodes

- [Trusted Policy Oversight](/Value_Alignment/Control/Oversight/Scalable_Oversight/Trusted_Policy_Oversight/Trusted_Policy_Oversight.md)
	- Reason: From Bounded Exploration also see Trusted Policy Oversight as bounded exploration may be a useful component of that.
