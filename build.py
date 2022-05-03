import io
import json
import requests
import pandas as pd

url = "https://digital.nhs.uk/binaries/content/assets/website-assets/services/nhs-mail/secure-email-standard/dcb1596_accredited_domains.xlsx"

r = requests.get(url)

with io.BytesIO(r.content) as fh:
    df = pd.io.excel.read_excel(fh, sheet_name=0)

orgs = {}

for row in df.itertuples():
    d = {
        "org": row[1],
        "intl_proc": (row[4] == "Yes"),
        "dmarc": row[5],
        "spf": row[6],
        "dkim": row[7] == "Y",
        "tls12": row[8] == "Y",
    }

    orgs[row[3].strip().lower()] = d

with open("orgs.json", "w") as f:
    json.dump(orgs, f)
