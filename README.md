# LIGO Noise Coherence Analysis Tool

This repository contains a data science pipeline developed for analyzing environmental and instrumental coherence in the Laser Interferometer Gravitational-Wave Observatory (LIGO). The tool helps identify noise channels that may interfere with gravitational wave detection.

## Overview

LIGO is the world’s leading scientific observatory for detecting gravitational waves—ripples in spacetime caused by events such as black hole mergers and neutron star collisions. To ensure accurate detections, it is essential to identify and mitigate environmental and instrumental noise.

This project focuses on analyzing coherence between LIGO’s gravitational wave channel and over 30 environmental/equipment sensors, with special attention to magnetic noise sources.

## ⚠️ Data Confidentiality Notice

**The original experimental data used in this project was obtained from the LIGO O4 Observation Cycle and is confidential. Access is restricted to designated LIGO research members and affiliated faculty. The data is not included in this repository.**

## Key Features

- Compute magnitude-squared coherence using Welch's method
- Analyze stochastic noise from both environmental and instrumental sources
- Automatically scan sensor pairs to detect high-coherence frequency bands
- Generate heatmaps to visualize coherence trends across more than 30 channels
- Export flagged results for review

## Repository Contents

- `coh_Mag_Entries-0711-0714 copy.ipynb`: Jupyter Notebook for coherence visualization and exploratory data analysis.
- `CoherenceChecker_Back.py`: Backend script for coherence computation and threshold-based flagging.

## Technologies Used

- Python 3.x
- NumPy
- Pandas
- SciPy
- Matplotlib
- Jupyter Notebook

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/LIGO-noise-coherence-analysis.git
   cd LIGO-noise-coherence-analysis
