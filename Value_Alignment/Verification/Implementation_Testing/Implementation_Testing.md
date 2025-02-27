### Mini Description

Techniques for testing implementations, including unit testing, integration testing, functional testing, system testing, stress testing, performance testing, and regression testing

### Description

Typical dynamic testing of software implementations include unit testing, integration testing, functional testing, system testing, stress testing, performance testing, and regression testing. These same kinds of tests can and should be applied to AI systems and agents ([Sculley et al. 2014](http://research.google.com/pubs/archive/43146.pdf)). While the levels of indirection concomitant to AI mean their domains and ranges are much too large to test exhaustively or even representatively, there remains value in this mode of quality assurance. Though not ostensibly representative of the distributions of what the agent can encounter, unit tests, for instance, can catch some representative failure modes that can be as elaborate and appropriate to the agent's complexities as can be imagined ([Coelho et al. 2006](https://pdfs.semanticscholar.org/363c/c023e00467141712292d9ecafa15acd78b25.pdf)). In contrast to the central role unit testing takes with most software development processes, it cannot be relied on to provide assurance for AI agents, and especially not advanced agents that support multiple layers of indirection. When verifying physical systems, or more generally any system properly subject to an open world model, particular cognizance needs to be paid to validating that the specification is complete.

### Related Nodes

- [Automated Vulnerability Finding](/Value_Alignment/Verification/Automated_Vulnerability_Finding/Automated_Vulnerability_Finding.md)
