### Mini Description

Generating a correct-by-construction implementation of a system given from its formal specification

### Description

When people desire extremely high reliability, e.g. for autopilot software, they often use formal logical systems to maximize their certainty of implementation correctness ([DoD 1985](http://csrc.nist.gov/publications/history/dod85.pdf), [Russell et al. 2015](http://futureoflife.org/data/documents/research_priorities.pdf)). This is the correct-by-construction approach to software engineering, where a system is developed in tandem with a detailed formal specification and a proof of total correctness given that specification, usually by generating the system from the formal specification ([Lamsweerde 2000](http://doi.acm.org/10.1145/336512.336546)). Creating a provably correct implementation, given a specification, is applicable for a range of layers of the software stack ([Fisher 2012](http://dl.acm.org/citation.cfm?id=2402695), [Baier and Katoen 2008](https://mitpress.mit.edu/books/principles-model-checking), [Clarke et al. 2017](http://www.springer.com/gp/book/9783319105741)). The seL4 kernel, for example, is a complete, general-purpose operating system kernel that has been mathematically checked against a formal specification to give strong guarantees against crashes and unsafe operations ([Klein et al. 2009](http://web1.cs.columbia.edu/~junfeng/09fa-e6998/papers/sel4.pdf)). For systems or agents that operate in environments that are at best only partially known by the system designer, it may still be practical to verify that the system acts correctly *given the knowledge that it has* , which avoids the problem of modelling the real environment ([Dennis et al. 2013](http://repository.liv.ac.uk/13195/1/verification_arxiv.pdf)) but puts much stronger onus on the formal specification to be valid.

### Related Nodes

- [Verified Downstack Software](/Value_Alignment/Security/Standard_IT_Security/Verified_Downstack_Software/Verified_Downstack_Software.md)
	- Reason: From Formal Software Verification also see Verified Downstack Software since having the lower layers of a system being verified often gets much of the benefit with appreciably less overhead.
