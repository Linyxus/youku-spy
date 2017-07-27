#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tools
import json

orig_urls = [ ]
for x in range(1, 31):
    print("# Generating Urls... (%d/30)" % x)
    orig_urls.append('http://list.youku.com/category/show/c_97_s_1_d_2_p_'+ str(x) +'.html')

codes = [ ]

for x, url in enumerate(orig_urls):
    print("# Fetching urls from pages... (%d/30)" % (x + 1))
    fetched_urls = tools.fetchUrls(url)
    print("## Total fetched: %d" % len(fetched_urls))
    code = tools.parseUrls(fetched_urls)
    print("## Invalid code parsed: %d" % len(code))
    list(map(lambda x: codes.append(x), code))

codes = list(set(codes))
total = len(codes)
print("# Total invalied code: %d" % total)

datas = [ ]

for x, code in enumerate(codes):
    print("# Fetching data for %s (%d/%d)" % (code, x + 1, total))
    datas.append(tools.getData(code))

print("# Fetching finished. Saving to file: data.json")
f = open('data.json', 'w')
f.write(json.dumps(datas))
f.close()
