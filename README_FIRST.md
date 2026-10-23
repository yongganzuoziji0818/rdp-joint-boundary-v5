# V5 companion code and constructed evidence

Companion work: **Joint completion-time guarantees for online relief distribution: a network obstruction and a tight tree budget**.
Authors: Yuan Liao, Hui Liu, Jiliang Tu, Haixing Wang. Contribution version: RDP_JOINT_BOUNDARY_V5_20261023.

This release consolidates two byte-unchanged scientific archives. Original code is licensed under MIT; original constructed inputs, results and documentation are licensed under CC BY 4.0. See LICENSE, DATA_LICENSE.md and LICENSE_SCOPE.json. Historical private-candidate labels and license-pending statements inside the frozen archives describe their original preparation state; the root licenses govern this authorized release. No earlier paper's DOI identifies this study.

## Contents and coverage

- `rdp_no_slowdown_v4_reproducibility_candidate_r2.zip`: the general-network part retained in V5. Its internal V4 labels and earlier working title intentionally remain unchanged for provenance. It includes frozen inputs and complete reference outputs for 240 constructed task executions, 20 parameter points, and an algebra addendum with 58 encoded witnesses and nine identities. These are not field data or independent statistical samples. Optional certificate regeneration alone requires SymPy 1.14.0.
- `tree_reader_v5_candidate_v1.zip`: three unchanged tree worker/auditor pairs, frozen inputs, complete trajectories, offline witnesses and reference results. The qualified reader replays 4,317 existing records, including 4,168 reference qualifications; it also reads old records for the snapshot audit. Replays do not create new independent scientific samples.

Normal reader checks require Python 3.10+ and the standard library only. No network, installation, GPU, weights or credentials are needed. Each inner README gives the full scope, limitations and commands. The general-network replay excludes only four explicitly enumerated timing fields from scientific-value equality; the tree replay compares twelve scientific output files byte-for-byte with no timing-field exemption. These comparison contracts differ and are not silently combined.

## Integrity and extraction

From this directory:

    python -B verify_and_extract.py
    python -B verify_and_extract.py --dest ./fresh_reader

The first checks the outer SHA-256 index and every ZIP member's CRC without executing scientific code. The second also extracts both archives into a nonexistent destination, in `general_network/` and `trees/`. It refuses an existing destination. Then, from either extracted component root:

    python -B reproduce.py --verify-only
    python -B reproduce.py --out ./fresh_results

Only the last command reexecutes scientific checks; use a fresh output directory and retain failures. For the rational certificate audit, follow `general_network/algebra/README.md`. No claim of full theorem formalization, universal policy enumeration, novelty certification or real-disaster validation is made.

## Attribution and provenance

These are the project's exact-arithmetic implementations, not the original RDP authors' program. Task source: Neugebauer, Otto and Schmidt, *The relief distribution problem with trucks and drones under incomplete demand information*, arXiv:2603.23135v1, https://arxiv.org/abs/2603.23135v1 . External papers, figures, dependencies, private server records, credentials and author-administration documents are excluded. Source snapshots inside the algebra addendum predate current exposition and remain unchanged. Computational reexecution is distinct from independent human mathematical review.

Repository: https://github.com/yongganzuoziji0818/rdp-joint-boundary-v5 . Version: v5.1.0. This release makes the bounded evidence accessible; it does not establish peer review, final author proof verification, or acceptance of the companion manuscript. Reader scripts do not contact external services or create repository records. A new Zenodo archive is handled separately, and its public record is authoritative only after publication.
