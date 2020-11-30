from clips import Environment, Symbol
import asyncio
import re

class Analysis:
	def __init__(self, clp_file_name):
		self.environment = Environment()
		self.get_result = []
		self.facts = [] #ini array2D of string
		self.environment.load(clp_file_name)
		self.environment.reset()

	def create_facts(self, i, j, value):
		facts = ['namatemplate',i,j,value]
		self.environment.assert_string(self.list_to_fact(facts))
		return 

	def assertFacts(self,facts):
		for fact in facts:
			self.environment.assert_string(self.list_to_fact(fact))
	
	def list_to_fact(self,facts):
		res = '('
		for idx, element in enumerate(facts):
			res += str(element)
			if(idx != len(facts)-1):
				res += " "
		res += ')'
		return res
	
	def show_facts(self):
		res = ""
		for fact in self.facts:
			res += (self.list_to_fact(fact))
			res += "\n"
		print(res)
		return res

	def show_rules(self):
		res = ""
		for rule in self.environment.rules():
			res += rule.name
			res += "\n"
		print("Rule list:")
		print(res)
	
	def print_rule(self, iteration, rule):
		res = (' '*iteration + rule)
		res += '\n'
		self.done[rule] = True
		for rule in self.rule_list[rule]:
			if not(self.done[rule]):
				res += self.print_rule(iteration+1, rule)
		return res

	def hit_rules(self):
		self.done = dict.fromkeys(self.rule_list, False)
		res = ""
		for rule in self.rule_list:
			if not(self.done[rule]):
				res += self.print_rule(0, rule)
		print("Hit rules:")
		print(res)
		return res

	def matched_facts(self):
		facts = []
		res = ""
		for fact in self.environment.facts(): # fact -> (down (value val) (x x) (y y))
			res += "f-" + str(fact.index) + " " + str(fact)
			res += '\n'
			
			listattr = fact.split("(")
			if(listattr[1] == "choose-cell "):
				action = listattr[2].split(" ")[1].replace(")","").replace(" ","")
				x = int(listattr[3].split(" ")[1].replace(")",""))
				y = int(listattr[4].split(" ")[1].replace(")",""))
				facts.append([action,x,y])
		# print("Matched facts:")
		# print(res)
		return fact

	def get_name(self, rule):
		return rule.name+' '+rule.__repr__().split(':')[2]

	def run(self):
		self.rule_list = dict.fromkeys([self.get_name(rule) for rule in self.environment.activations()], [])
		while(len([rule for rule in self.environment.activations()])):
			activations = self.environment.activations()
			current_rule = next(activations)
			rule_name = self.get_name(current_rule)
			self.environment.run(1)
			self.update_rule_matched(rule_name)

	def update_rule_matched(self, rule_name):
		if(not(rule_name in self.rule_list.keys())):
			self.rule_list[rule_name] = []
		for activation in self.environment.activations():
			if(not(self.get_name(activation) in self.rule_list.keys())):
				self.rule_list[self.get_name(activation)] = []
				self.rule_list[rule_name].append(self.get_name(activation))
