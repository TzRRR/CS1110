# Tianze Ren tr2bx
def gellish2 (age):
    return 191.5-(0.007 * age**2)


def in_target_range(hr,age):
    hrmax = gellish2(age)
    targetsmall = hrmax * 0.65
    targetbig = hrmax * 0.85
    return hr >= targetsmall and hr <= targetbig


