#https://www.codewars.com/kata/esolang-tick/train/python	

from collections import defaultdict
def interpreter(tape):
    memory, potr, res = defaultdict(int), 0, []
    for cmd in tape:
        if cmd == '+':
            memory[potr] += 1
        elif cmd == '*':
            res.append(chr(memory[potr] % 256))
        elif cmd == '>':
            potr += 1
        elif cmd == '<':
            potr -= 1
    return ''.join(res)
