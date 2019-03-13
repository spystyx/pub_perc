import pandas as pd

w1 = 4.0
w2 = 4.0
bx = 1.0


tIN = [(0, 0), (0, 1), (1, 0), (1, 1)]
cOUT = [False, False, False, True]
os = []
for test_input, Co in zip(tIN, cOUT):
    lc = w1 * test_input[0] + w2 * test_input[1] + bx
    o = int(lc >= 0)
    is_correct_string = 'Yes' if o == Co else 'No'
    os.append([test_input[0], test_input[1], lc, o, is_correct_string])

# Print o
num_wrong = len([o[4] for o in os if o[4] == 'No'])
output_frame = pd.DataFrame(os, columns=['Input 1', '  Input 2', '  LC', '  Activation Output', '  Is Correct'])
if not num_wrong:
    print('Nice!  You got it all correct.\n')
else:
    print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
print(output_frame.to_string(index=False))
