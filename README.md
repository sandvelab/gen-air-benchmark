# Profiling of AIRR Generative Models

This repository contains the code accompanying the manuscript:

> **What Do Generative Models Learn About Adaptive Immune Receptor Repertoires? A Benchmark Study**
> bioRxiv, 2026. [doi: https://doi.org/10.64898/2026.07.10.737788](https://doi.org/10.64898/2026.07.10.737788)

## Overview

Generative models of Adaptive Immune Receptor Repertoire (AIRR) data are increasingly used to
simulate receptor sequences, and reason about the relationship between sequence diversity and immune responses.
How to *evaluate* such models, however, remains poorly standardised.

This work addresses that gap in two parts:

1. **Evaluation methodology**: we assess which repertoire-level statistics and distributional
   comparisons are informative for judging generative AIRR models.
2. **Model profiling**: we apply this evaluation to widely used model families in the field
   (VAE, LSTM, and soNNia), characterising their outputs against empirical immune receptor
   datasets and identifying systematic tendencies and failure modes.

## Installation

```bash
git clone https://github.com/sandvelab/gen-airr-profiling.git
cd gen-airr-profiling

conda create -n gen_airr_bm python=3.11
conda activate gen_airr_bm

pip install -r requirements.txt
pip install -e .
```

## Running dummy example

```bash
python3 gen_airr_bm/pipelines/generic_pipeline.py configs/dummy_pipelines/experimental_1.yaml --no_parallel
```

## Repository structure

```
.
├── adhoc_analysis/      # Code for running adhoc analysis not part of the core pipeline
├── configs/             # Config files containing specification for all analyses run
├── data/                # Dummy data for running the dummy pipeline
├── gen_airr_bm/         # Core, data generation, pipeline, training, analysis, and evaluation code
└── requirements.txt     # Listed packages for reproducible environment. 
```
