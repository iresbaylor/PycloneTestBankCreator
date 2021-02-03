from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
import ast
import pprint
import astor

from logic.common import construct_output_file


def create_type_2(filename, output_path):
    # read the file into an ast
    tree = astor.code_to_ast.parse_file(filename)

    # copy the tree to prepare for modification
    mod_tree = tree

    # print original tree
    # print(astor.dump_tree(mod_tree))
    #
    # print("\n***\n")

    # modify the variable names then print modified tree
    get_mod_tree(astor.dump_tree(mod_tree))

    # convert the modified tree dump to code
    # astor.to_source(rename_variables(astor.dump_tree(mod_tree), indent_with=' ' * 4, add_line_information=True))

    # print the modified code to the console from the tree
    # print(astor.to_source(mod_tree, indent_with=' ' * 4, add_line_information=False))

    # Construct & print output
    print('printing output of type 2 comparison')
    new_filename = construct_output_file(filename, output_path)
    with open(new_filename, 'w') as fw:
        fw.write(mod_tree.__str__())


def get_mod_tree(tree):
    mods = tree.split("\n")
    # indicates the next value is the variable name
    var_name_next = "Name(id=\'"
    var_num = 0
    mod_tree = ""
    for s in mods:
        # number of variable names in this line
        var_name_count = s.count(var_name_next)

        # isolate the nodes that contain a variable or function name
        if var_name_count > 0:
            # split the line right where the variable name would begin
            var_names = s.split(var_name_next)
            mod_line = ""
            i = 0
            while i < len(var_names)-1:
                # change each variable name to var + arbitrary number
                mod_line += var_names[i] + var_name_next + "var" + var_num.__str__() + "\'"
                # change each var arbitrary number
                var_num += 1
                # add on the rest of the line
                mod_line += var_names[i+1].split('\'', 1)[-1]
                i += 2
            # print the modified tree line to console
            print(mod_line)
            # add the modified dump line to the mod tree dump
            mod_tree += mod_line
        else:
            # print the same tree line to console
            print(s)
            # add the original dump line to the mod tree dump
            mod_tree += s
    # return the modified tree dump
    return mod_tree
