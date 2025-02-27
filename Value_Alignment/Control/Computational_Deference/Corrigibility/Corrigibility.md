### Mini Description

Methods by which an advanced agent can be built with sufficient incentives to allow its operators to correct it despite otherwise being subject to the default convergent instrumental incentives to prevent such changes

### Description

Another natural subgoal for AI systems pursuing a given goal is the acquisition of resources of a variety of kinds. For example, information about the environment, safety from disruption, and improved freedom of action (such as by additional compute power) are all instrumentally useful for many tasks ([Omohundro 2007](http://selfawaresystems.files.wordpress.com/2008/01/nature_of_self_improving_ai.pdf), [Bostrom 2012](http://www.nickbostrom.com/superintelligentwill.pdf)). By default, an advanced agent has incentives to preserve its own preferences, even if those happen to conflict with the actual intentions of its developers ([Omohundro 2008](https://selfawaresystems.files.wordpress.com/2008/01/ai_drives_final.pdf)). Uncommon kinds of reasoning may be required to reflect the fact that an agent is incomplete and potentially flawed in dangerous ways ([Soares and Fallenstein 2014](http://intelligence.org/files/QuestionsLogicalUncertainty.pdf), [Soares and Fallenstein 2014a](http://intelligence.org/files/TechnicalAgenda.pdf)), and this would seem to be the most robust way to enable such agents to allow operators to correct their objective functions. In one approach, for example, the agent may need to consider counterfactuals for each effect of an action in order to finally ignore the effects of a given channel ([Jessica and Olah 2016](https://agentfoundations.org/item?id=735)). There may also be a path to a similar effect via differentially private multiarmed bandits (a prioritization mechanism where private information is connected to individual rewards, [Tossou and Dimitrakakis 2016](http://www.aaai.org/Library/AAAI/aaai16contents.php)).

### Related Nodes

- [Goal Stability](/Value_Alignment/Foundations/Consistent_Decision_Making/Goal_Stability/Goal_Stability.md)
- [Error-Tolerant Agent Design](/Value_Alignment/Validation/Averting_Instrumental_Incentives/Error-Tolerant_Agent_Design/Error-Tolerant_Agent_Design.md)
- [Consistent Decision Making](/Value_Alignment/Foundations/Consistent_Decision_Making/Consistent_Decision_Making.md)
	- Reason: From Corrigibility also see Consistent Decision Making as those considerations, e.g. goal stability, are formidable prerequisites to corrigibility.
