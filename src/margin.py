import sys

from dot_parser import parse_dot

if len(sys.argv) < 2:
    raise ValueError("No .dot file specified")

markov_chain_dot_file_path = sys.argv[1]

# load .dot file
markov_chain_dot = ''
with open(markov_chain_dot_file_path, 'r') as markov_chain_dot_file:
    markov_chain_dot = markov_chain_dot_file.read().replace('\n', '')

# parse .dot file
markov_chain = parse_dot(markov_chain_dot)

# build dictionary storing adjacency matrix
states = {}
for edge_rule in markov_chain['edge_rules']:
    if edge_rule['origin_state_name'] not in states:
        states[edge_rule['origin_state_name']] = []
    states[edge_rule['origin_state_name']].append({
        'destination_state_name' : edge_rule['destination_state_name'],
        'transition_probability' : edge_rule['transition_probability'],
    })

# generate markov chain code
markov_chain_code = ""

markov_chain_code += "class " + markov_chain['name'] + ":\n"

markov_chain_code += "\tdef __init__(self, initial_state):\n"
#markov_chain_code += "\t\tself.states = " + str(states) + "\n"
markov_chain_code += "\t\tself.curr_state = initial_state\n"

markov_chain_code += "\n"

markov_chain_code += "\tdef step(self, probability):\n"
is_first_state = True
for state_name, edges in states.items():
    if is_first_state:
        markov_chain_code += "\t\tif self.curr_state == " + state_name + ":\n"
        is_first_state = False
    else:
        markov_chain_code += "\t\telif self.curr_state == " + state_name + ":\n"

    total_probability = 0
    for edge in edges:
        total_probability += edge['transition_probability']

    cumulative_probability = 0
    for i, edge in enumerate(edges):
        cumulative_probability += edge['transition_probability']
        if i == 0:
            markov_chain_code += "\t\t\tif probability < " + str(edge['transition_probability'] / total_probability) + ":\n"
        else:
            markov_chain_code += "\t\t\telif probability < " + str(edge['transition_probability'] / total_probability) + ":\n"
        markov_chain_code += "\t\t\t\tself.curr_state = " + edge['destination_state_name'] + "\n"

markov_chain_code += "\n"

# print generated code to new file
markov_chain_code_file_path = markov_chain_dot_file_path.replace(".dot", ".py")
markov_chain_code_file = open(markov_chain_code_file_path, 'w')
markov_chain_code_file.write(markov_chain_code)
markov_chain_code_file.close()
