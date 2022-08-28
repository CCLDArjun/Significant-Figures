from sigfigs import Val as v

things = ['5.0', '5.00', '5.000', '5.0000', '0.5', '0.50', '0.500', '5']
fail = False

for t in things:
    val = v(t)
    if not v(val.__repr__()).sig_figs == val.sig_figs:
        print(f'ERROR: {t}\n  actual_sigfigs: {val.sig_figs}\n  repr_sigfigs  : {v(val.__repr__()).sig_figs}\n   repr: {val.__repr__()}\n')
        fail = True
        
if not fail:
    print("All tests passed",)

