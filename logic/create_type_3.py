import astor
import random


def create_type_3(filename, output_path):
    p = astor.code_to_ast.parse_file(filename)
    modify_tree(astor.dump_tree(p))


def modify_tree(tree):
    # find operators, switch them
    # BoolOp(op=And, op=Or
    # ops=[GtE], ops=[Eq], ops=[LtE], [Lt], [Gt], [Is], [IsNot], [NotEq]
    # op=Add, Sub, Mult, Div, Mod

    lines = tree.split("\n")
    indicators = ["BoolOp(op=", "ops=[", "op="]
    opsOpt = ["GtE", "Eq", "LtE", "Lt", "Gt", "Is", "IsNot", "NotEq"]
    opOpt = ["Add", "Sub", "Mult", "Div", "Mod"]
    new_tree = ""
    for l in lines:
        c1 = l.count(indicators[0])
        c2 = l.count(indicators[1])
        c3 = l.count(indicators[2])

        tLine = ""
        if c1 > 0:
            pieces = l.split(indicators[0])
            tLine += pieces[0]
            if l.count("And") > 0:
                tLine += "Or,"
            elif l.count("Or") > 0:
                tLine += "And,"
            # put rest of stuff back in
            secondhalf = pieces[1].split(",")
            i = 1
            remain = len(secondhalf)
            while remain > 1:
                tLine += secondhalf[i]
                i += 1
                remain -= 1
            new_tree += tLine+"\n"
        elif c2 > 0:
            firsthalf = l.split(indicators[1])
            tLine += firsthalf[0]
            secondhalf = l.split("]")
            rnum = random.randrange(8)
            tLine += "ops=[" + opsOpt[rnum] + "]"
            # put the rest of the stuff back in
            i = 1
            remain = len(secondhalf)
            while remain > 1:
                tLine += secondhalf[i]
                i += 1
                remain -= 1
            new_tree += tLine+"\n"
        elif c3 > 0:
            firsthalf = l.split(indicators[2])
            tLine += firsthalf[0]
            secondhalf = l.split(",")
            rnum = random.randrange(5)
            tLine += "op=" + opsOpt[rnum] + ","
            # put the rest of the stuff back in
            i = 1
            remain = len(secondhalf)
            while remain > 1:
                tLine += secondhalf[i]
                i += 1
                remain -= 1
            new_tree += tLine+"\n"
        else:
            new_tree += l+"\n"
    print(new_tree)