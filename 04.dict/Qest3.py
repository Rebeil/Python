#!/usr/bin/env python3

results = {
    'vk': {'revenue': 103,
           'cost': 98},
    'yandex': {'revenue': 179,
               'cost': 153},
    'facebook': {'revenue': 103,
                 'cost': 110},
    'adwords': {'revenue': 35,
                'cost': 34},
    'twitter': {'revenue': 11,
                'cost': 24},
}
# (revenue / cost - 1) * 100

for social in results.values():
    a = list(social.values())
    # noinspection PyTypeChecker
    social['ROI'] = (a[0] / a[1] - 1) * 100

for i in results.values():
    print(i)
