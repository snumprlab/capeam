import glob
import pickle

templates = ['div24_seed0']

def f(template, split=None):
    splits = ['valid_seen', 'valid_unseen', 'tests_seen', 'tests_unseen'] if split is None else [split]
    for split in splits:
        success, total = 0, 0
        for p in glob.glob(f'results/analyze_recs/{split}*{template}*'):
            r = pickle.load(open(p, 'rb'))
            success += sum([s['success'] for s in r])
            total += len(r)
        print(split, success, total, success / total)

for template in templates :
    print('##################')
    print(template)
    for split in ['valid_seen', 'valid_unseen', 'tests_seen', 'tests_unseen']:
        try:
            f(template, split)
        except:
            pass
