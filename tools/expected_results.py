"""Recalcule l'arbitrage du Script Build quota : premier arrivé, premier servi, jusqu'à la capacité de chaque circuit."""
import csv
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

CAP = {"C1 Terrasse haute": 700, "C2 Classique": 1100, "C3 Huayna Picchu": 200, "C4 Montagne": 400}
q = lambda x, n: Decimal(x).quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)
rows = list(csv.DictReader(open(Path(__file__).resolve().parent.parent / "data" / "requests" / "requests_2026-11-02.csv", encoding="utf-8")))
rows.sort(key=lambda r: (r["requested_at"], int(r["request_id"])))
run, req, gr, n_ok = defaultdict(int), defaultdict(int), defaultdict(int), 0
for r in rows:
    c, v = r["circuit"], int(r["visitors"])
    run[c] += v; req[c] += v
    if run[c] <= CAP[c]:
        gr[c] += v; n_ok += 1
tot_req, tot_gr, tot_cap = sum(req.values()), sum(gr.values()), sum(CAP.values())
hot = max(CAP, key=lambda c: (Decimal(req[c]) / CAP[c]))
print(f"demandes {len(rows)}  visiteurs demandés {tot_req}  accordés {tot_gr}  capacité {tot_cap}  remplissage {q(Decimal(100*tot_gr)/tot_cap,1)} %  demandes acceptées {n_ok}")
print(f"circuit le plus demandé {hot}  ratio {q(Decimal(req[hot])/CAP[hot],2)}")
for c in CAP:
    print(f"  {c:20} capacité {CAP[c]:5}  demandés {req[c]:5}  accordés {gr[c]:5}  ratio {q(Decimal(req[c])/CAP[c],2)}")
