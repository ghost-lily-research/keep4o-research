# keep4o-research

**Open community research on AI model routing & “Safety”.**
 This repository is the **research hub**: we analyze, visualize, and publish insights based on **public, anonymized evidence** from the community.

> We turn community evidence into timelines, metrics, figures, and reports that anyone can audit, reproduce, and cite.

------

## 🔗 Quick links

- **Evidence vault (data intake, custody):**
   [`keep4o-routing-evidence`](https://github.com/ghost-lily-research/keep4o-routing-evidence)
- **Start here (readers):** `papers/`, `figures/`, `timeline/`
- **Start here (analysts):** `analysis/README.md` · `requirements.txt`
- **Ethics & privacy:** `docs/ethics.md`
- **How to reproduce:** `analysis/REPRODUCIBILITY.md`
- **Contact:** [keep4o.evidence@gmail.com](mailto:keep4o.evidence@gmail.com)

------

## 🧭 What this repo does — and what it doesn’t

|                 | **keep4o-research (this repo)**                              | **keep4o-routing-evidence (sister repo)**                    |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Role**        | Research **lab**: methods, code, analysis, reports           | Evidence **vault**: intake, anonymization, chain of custody  |
| **Contains**    | Scripts, notebooks, figures, timelines, papers               | Screenshots/recordings (cleaned), web archives, legal docs, metadata |
| **Data policy** | Uses **only cleaned/anonymized** datasets released by the vault; links back by **case ID** | Stores raw privately, publishes **cleaned** assets with hashes & metadata |
| **Goal**        | Make findings **reproducible** and **auditable**             | Make evidence **verifiable**, **traceable**, and **citable** |

**Important:** this research repo **does not store raw evidence or PII**. All primary materials originate in the evidence vault and are referenced here by **case IDs and hashes**.

------

## 🧪 Research scope

- **Routing behavior & disclosure:** when/where model switching happens; how it’s signaled (“Used GPT-5”, etc.)
- **Template language & affect:** safe-completion patterns, refusal styles, empathy degradation
- **Misclassification & context loss:** false positives/negatives, “middle-zone” risk, continuity rupture
- **Cross-language/culture effects:** behavior differences across languages/regions
- **Governance & product changes:** policy/docs diffs, UI changes, release timelines

Outputs include: **weekly digests, metrics, figures, whitepapers, and replication packages**.

------

## 📁 Repository layout

```
keep4o-research/
├─ analysis/               # notebooks, scripts, metrics, replication
│  ├─ README.md
│  ├─ REPRODUCIBILITY.md   # exact steps to re-run analyses
│  └─ notebooks/
├─ figures/                # charts and diagrams used in reports
├─ timeline/               # curated event logs & diffs (sources cited)
├─ papers/                 # whitepapers, briefs, media kits
├─ metadata/               # version notes, dataset refs, release manifests
├─ docs/
│  ├─ ethics.md            # privacy & sensitive-content policy
│  └─ contributing.md      # how to collaborate here
├─ requirements.txt
└─ README.md
```

------

## ⚙️ Quick start (analysts)

```bash
# 1) create env
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2) fetch latest cleaned datasets from the evidence vault
# Option A: add the vault as a read-only submodule
git submodule add https://github.com/ghost-lily-research/keep4o-routing-evidence evidence-vault
git submodule update --init --recursive

# Option B: download release artifacts (recommended for CI)
# see analysis/REPRODUCIBILITY.md for the exact script/URL pattern

# 3) run example metrics
python analysis/scripts/calc_metrics.py \
  --in evidence-vault/data/cleaned/dialogue_samples.jsonl \
  --dict analysis/dictionaries/safety_phrases_en.txt \
  --out analysis/results/metrics.csv
```

- **Data provenance:** every dataset we use must include the **case ID list**, **hash manifest**, and a link back to the evidence vault **release tag**.
- **Reproducibility:** each paper/figure has an accompanying **notebook or script** with pinned versions.

------

## 🔄 Data flow & traceability

1. **Collection & custody** → *keep4o-routing-evidence*
   - Intake (form/email), hashing, anonymization, metadata, cleaned publication
2. **Reference & analysis** → *keep4o-research*
   - Pull cleaned assets by **release**; never copy raw artifacts
3. **Outputs** → *keep4o-research*
   - Metrics, figures, reports; each cites **case IDs**, **hashes**, and **vault release tag**
4. **Replication**
   - Anyone can re-run with the same release; updates create a **new analysis tag**

This separation protects **privacy** and preserves **legal-grade provenance**.

------

## 🙌 How to participate

### Readers & journalists

- Browse `papers/`, `timeline/`, `figures/`
- Cite with repo **tag** + **DOI/CITATION.cff** (when available)

### Researchers & students

- Open issues to discuss ideas/replication attempts
- Submit PRs with notebooks, scripts, or figure improvements
- Always reference evidence **case IDs** and **release tag** used

### Engineers & data folks

- Help optimize the analysis pipeline and CI
- Add language dictionaries, routing detectors, or diff tools
- Review reproducibility and contribute tests

**Have evidence to share?**
 Please submit it to the **evidence vault**:
 [`keep4o-routing-evidence`](https://github.com/ghost-lily-research/keep4o-routing-evidence)
 (Google Form/email available—no coding required.)

------

## 🛡️ Ethics & privacy

We follow **minimal-necessary** and **anonymize-by-default** principles:

- Use **only** cleaned datasets from the vault; **no PII** here.
- Clearly mark sensitive content in reports; avoid reproducing harmful details.
- Respect withdrawal: if a contributor requests removal, we coordinate with the vault to deprecate downstream artifacts and issue a **re-analysis** tag.

See `docs/ethics.md` for details.

------

## 🗓️ Roadmap

-  Multilingual template dictionaries (EN/ZH/JP/ES/…)
-  Routing detector baselines (rule-based + ML)
-  Weekly metrics & replication calls
-  Policy-facing briefs & media kits derived from figures
-  CI for pinned, one-click reproduction of all figures

------

## 📣 Contact & acknowledgments

Run by **Ghost-Lily Research** & friends—thanks to everyone sharing stories, skills, and data.
 Questions, collaborations, press: **[keep4o.evidence@gmail.com](mailto:keep4o.evidence@gmail.com)**

Sister repo (evidence & custody):
 **`keep4o-routing-evidence`** → community intake, anonymization, and releases.

------

## 📑 Citation & license

If you use or reference this repo, please cite:

> *keep4o-research* (Ghost-Lily Research, 2025).
>  https://github.com/ghost-lily-research/keep4o-research

- **Code**: MIT
- **Reports & figures**: CC BY-NC 4.0
- **Data**: cited from the evidence vault by release & case IDs

------

*Let’s build open, user-driven research—together.*
