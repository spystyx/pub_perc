import pandas as pd

w1 = 4.0
w2 = 4.0
bx = 1.0


tIN = [(0, 0), (0, 1), (1, 0), (1, 1)]
cOUT = [False, False, False, True]
os = []
for tst_in, Co in zip(tIN, cOUT):
    lc = w1 * tst_in[0] + w2 * tst_in[1] + bx
    o = int(lc >= 0)
    ch_srg = 'Yes' if o == Co else 'No'
    os.append([tst_in[0], tst_in[1], lc, o, ch_srg])

num_wrong = len([o[4] for o in os if o[4] == 'No'])
out_frm = pd.DataFrame(os, columns=['Input 1', '  Input 2', '  LC', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(out_frm.to_string(index=False))
