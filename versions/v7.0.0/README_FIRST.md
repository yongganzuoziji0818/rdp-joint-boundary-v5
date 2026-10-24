# V7 companion code and constructed evidence — v7.0.0

Budget and competitive guarantees for online truck-drone relief distribution: V7 companion code and constructed evidence

Authors: Yuan Liao, Hui Liu, Jiliang Tu, Haixing Wang.
Version DOI: https://doi.org/10.5281/zenodo.23607213
Repository: https://github.com/yongganzuoziji0818/rdp-joint-boundary-v5/releases/tag/v7.0.0

## Run

Python 3.10 or later; standard library only. The full reader replay has been qualified on Linux CPU. Windows full replay is not certified. No network, installation, GPU or training is needed for normal checks.

First verify/extract the inner reader into a fresh directory:

```
python -B verify_and_extract.py --out ./reader
cd reader
python -B reproduce_all.py --verify-only
python -B reproduce_all.py --out ./fresh_results
python -B audit_replay.py --out ./fresh_results
```

Existing extraction/output directories cause a stop, not replacement. Preserve logs after an error. Optional regeneration of older algebra certificates requires SymPy 1.14.0, but normal verification does not.

## Contents and interpretation

The inner ZIP is the byte-unchanged, independently replayed complete reader (SHA-256 `3c8e08d58f61da36c8c5923151a04b73f4b85260ef4eb10be3e6f49c20cbef22`). It contains code, constructed inputs, frozen reference outputs, original comparison contracts and inner instructions. It replays 10,199 existing execution records, including the two-world illustration's eight records and 96 exact allocation rows. Reexecution does not add independent samples.

The package covers retained general-network and tree checks, root-spider policies, source-defined ordinary comparators, ordinary LPT and the two-world complete-task illustration. Exact finite checks qualify those implementations; they do not prove universal policy-class theorems. The two-world illustration is also resolved by ordinary tiny exhaustive allocation and is not a new solver.

Historical revision5/private-candidate identifiers and license-pending notices remain inside frozen components. Revision6 only clarifies proof prose and the manuscript date; formulas, scientific modules, inputs and results are unchanged. These root licenses govern newly authorized original V7 material, while existing V5 licenses remain in force.

## Scope and rights

Original scientific/reproduction Python code: MIT. Original constructed inputs, results and research documentation: CC BY 4.0. See LICENSE, DATA_LICENSE.md and LICENSE_SCOPE.json. No new manuscript PDF or full TeX source bundle is included. An older own-proof excerpt remains within the preserved, already published V5 component under its existing license.

No third-party papers, dependency distributions, credentials, private host records or author-review material are included. The source task is Neugebauer, Otto and Schmidt's RDP, arXiv:2603.23135v1, https://arxiv.org/abs/2603.23135v1 . These are this project's implementations, not runs of the source authors' unavailable repository.

The previous V5 version remains available at https://doi.org/10.5281/zenodo.23590304 . This V7 release is a version of the same study; it is separate from the older marginal-recurrence paper. No field-rescue gain, full formal proof, global novelty certification or journal acceptance is claimed.
