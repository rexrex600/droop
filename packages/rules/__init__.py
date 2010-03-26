'''
election rules module init

copyright 2010 by Jonathan Lundell
'''

#  for now, we have built-in knowledge of the available election rules;
#  at some point we'll scan the rules package for more rules
#
#  warren is a special case, since it shares the meek module with meek
#
electionRuleNames = ('meek', 'warren', 'wigm', 'mpls')

import meek
import mpls
import wigm

electionRules = dict(
    meek=meek.Rule,
    warren=meek.Rule,
    wigm=wigm.Rule,
    mpls=mpls.Rule
)

def electionRule(name):
    "convert a rule name to a rule class"
    return electionRules.get(name, None)

def helps(helps):
    "build a help-string dictionary"
    helps['rule'] =  'available rules: %s' % ','.join(electionRuleNames)
    for rule in electionRules:
        electionRules[rule].helps(helps)
