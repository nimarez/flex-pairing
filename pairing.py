import random


interests = ['intellectual', 'athletic']
demographics = ['race', 'gender', 'sex', 'family']
participants = []

for i in range(100):
    participants.append({category: [random.choice((-1, 1)) for _ in range(11)] for category in (interests + demographics)})
    


sim_scores = []
diff_scores = []
for i in range(len(participants)):
    for j in range(len(participants)):
        zipped_interests = [zip(participants[i][interest], participants[j][interest]) for interest in interests]
        sims = sum([sum([pair[0] * pair[1] for pair in dot]) for dot in zipped_interests])
        zipped_demographics = [zip(participants[i][demographic], participants[j][demographic]) for demographic in demographics]
        diffs = sum([sum([pair[0] * pair[1] for pair in dot]) for dot in zipped_demographics])
        sim_scores.append(sims)
        diff_scores.append(diffs)

score = sim_scores + diff_scores








