### Mini Description

How the values and preferences of an operator can be extracted, and the operator modeled as embedded in its environment, while increasing accuracy over time

### Description

In order to model an operator's preferences as comprehensively as possible, the operator themselves should be modeled well. By what methods can an operator be modeled in such a way that a model of the operators preferences can not only be extracted, but also continually refined to become arbitrarily accurate, while representing the operator as a subsystem embedded within the larger world? ([Soares 2016](https://intelligence.org/files/ValueLearningProblem.pdf)) There is work on modeling individuals' cognition ([Goodman and Tenenbaum 2016](http://probmods.org/v2)), progress in short-term modeling of, and adaptation to, operators ([Liu et al. 2016](http://www.jesshamrick.com/publications/pdf/Liu2016-Goal_Inference_Improves_Objective.pdf)), and modeling human preferences as inverse planning ([Baker et al. 2009](http://web.mit.edu/clbaker/www/papers/cognition2009.pdf)), but more work is needed to approach comprehensive modeling ([Soares and Fallenstein 2014a](http://intelligence.org/files/TechnicalAgenda.pdf)). One approach to prevent overfitting is to use different assumptions about underlying cognitive models of the actor whose preferences are being learned ([Chu and Ghahramani 2005](http://www.gatsby.ucl.ac.uk/%7Echuwei/paper/gppl.pdf)).

For complex tasks, it seems plausible that the system will need to learn a detailed psychological model of a human if it is to imitate one, and that this might be significantly more difficult than training a system to do engineering directly. More research is needed to clarify whether imitation learning can scale efficiently to complex tasks.

### Related Nodes

- [Value Specification](/Value_Alignment/Validation/Technical_Value_Alignment/Ethics_Mechanisms/Value_Specification/Value_Specification.md)
- [Operator Value Learning](/Value_Alignment/Validation/Technical_Value_Alignment/Ethics_Mechanisms/Value_Learning/Operator_Value_Learning/Operator_Value_Learning.md)
	- Reason: From Operator Modeling also see Operator Value Learning which is similar but focuses on learning the ethical or moral values of people rather than their broader dynamics.
- [Psychological Analogues](/Value_Alignment/Validation/Psychological_Analogues/Psychological_Analogues.md)
	- Reason: From Operator Modeling also see Psychological Analogues as there will likely be much cross-pollination between these threads.
