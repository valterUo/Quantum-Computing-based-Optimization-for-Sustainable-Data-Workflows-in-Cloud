import json
import random

cloud_partners_data = "cloud_partners_large.json"
f = open(cloud_partners_data)
partners_root = json.load(f)
cloud_partners = partners_root["cloud_partners"]

for partner in cloud_partners:
    for center in partner["data_centers"]:
        for work in center["workload_dependent_emissions"]:
            work.pop('emission_interval', None)
            work["center_emission_factor"] = random.randint(1, 40)

with open('json_data.json', 'w') as outfile:
    json.dump(partners_root, outfile)