from dataclasses import dataclass
from typing import Dict, List, Literal, Tuple


DEBUG = 1


# workflows, N = list(map(str.splitlines, open(
# './in/19.test.txt').read().split('\n\n')))
workflows, N = list(map(str.splitlines, open(
    './in/19.txt').read().split('\n\n')))


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int


@dataclass
class Rule:
    cond: Tuple[Literal['x', 'm', 'a', 's'], Literal['<', '>'], int] | None
    dest: str


@dataclass
class Workflow:
    _id: str
    rules: List[Rule]


parts: List[Part] = []
for line in N:
    tokens = line[1:-1].split(',')
    parts.append(Part(
        *(int(token[2:]) for token in tokens)
    ))


flows: Dict[str, Workflow] = {}

for line in workflows:
    _id, rules = line.split('{')
    rules = rules[:-1].split(',')

    flow = Workflow(_id, [])

    for rule in rules:
        if ':' not in rule:
            # just a destination
            flow.rules.append(Rule(
                None, dest=rule
            ))
            continue
        cond, dest = rule.split(':')

        if '<' in cond:
            test, value = cond.split('<')
            operator = '<'
        else:
            test, value = cond.split('>')
            operator = '>'

        flow.rules.append(Rule(
            (test, operator, int(value)),
            dest
        ))

    flows[_id] = flow


def evaluate(part: Part, workflow_id: str, flows=flows):
    if workflow_id in 'AR':
        return workflow_id
    workflow = flows[workflow_id]
    for rule in workflow.rules:
        if rule.cond is None:
            return evaluate(part, rule.dest)
        test, operator, value = rule.cond

        tval = getattr(part, test)
        if operator == '>':
            if tval > value:
                return evaluate(part, rule.dest)
        elif tval < value:
            return evaluate(part, rule.dest)
    else:
        raise Exception('Not supposed to get here')


def part_1():
    t = 0
    for part in parts:
        if evaluate(part, 'in') == 'A':
            t += part.x + part.m + part.a + part.s
    return t


def part_2():
    # ah fuck me, it's another reverse-engineering puzzle
    pass


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(part_1())
    print('\n--- Part 2 ---')
    print(part_2())
