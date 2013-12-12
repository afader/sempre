import re
import sys
data = dict()
qpat = re.compile(r'Example: (.*) \{')
ppat = re.compile(r'"(.*?)"')
spat = re.compile(r'score=([-0-9.]+)')
question = None
for line in sys.stdin:
    line = line.strip()
    if line.startswith('Example:'):
        question = qpat.findall(line)[0]
    if line.startswith('Pred@0000:'):
        answers = ppat.findall(line)
        score = float(spat.findall(line)[0])
        for a in answers:
            print '%s\t%s\t%s' % (question, a, score)
