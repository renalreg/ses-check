import csv
import json
from contextlib import closing
import requests

# Ok so super cool thing, NHS Digital have decided to keep the URL looking like an XLSX file, but it actually downloads a CSV file.
# The HTTP response downloads the file with a filename "dcb1596_accredited_domains.csv".
# Furthermore, it's full of non-UTF-8 characters, I assume because the file is being lazily converted from Excel to CSV
URL = "https://digital.nhs.uk/binaries/content/assets/website-assets/services/nhs-mail/secure-email-standard/dcb1596_accredited_domains.xlsx"

orgs = {}

with closing(requests.get(URL, stream=True)) as r:
    # NOTE: We need to add "ignore" to the decode to avoid exceptions where the file contains non-utf-8 characters
    f = (line.decode("utf-8", "ignore") for line in r.iter_lines())
    reader = csv.reader(f, delimiter=",", quotechar='"')
    next(reader, None)  # Skip headers
    for row in reader:
        if not row:
            continue

        d = {
            "org": row[0],
            "intl_proc": (row[3] == "Yes"),
            "dmarc": row[4],
            "spf": row[5],
            "dkim": row[6] == "Y",
            "tls12": row[7] == "Y",
        }

        orgs[row[3].strip().lower()] = d

with open("orgs.json", "w", encoding="utf-8") as f:
    json.dump(orgs, f)
