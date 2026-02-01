# Agentic Galactic Discovery (AGD)

> **Real-time astronomical transient detection, classification, and anomaly discovery using agentic AI over streaming telescope data.**

## Vision

Agentic Galactic Discovery is an open-source platform that connects real-time astronomical alert streams to AI-powered analysis agents. The system ingests transient event data from major surveys (ZTF now, Rubin/LSST imminently), processes it through a Databricks lakehouse architecture, and deploys LLM-orchestrated agents that classify, cross-reference, and flag scientifically interesting events — especially anomalies that challenge existing theoretical frameworks.

The project exists in the spirit of open science: the data is public, the tools are open-source, and the goal is genuine discovery. We build on the shoulders of giants and contribute back.

## Why Now?

- **Rubin/LSST alert stream begins early 2026** — expected to generate ~10 million alerts per night, a 10x increase over ZTF
- **ZTF currently streams ~1 million alerts/night** via Apache Kafka, providing an immediate testbed
- **Community brokers** (Fink, ANTARES, ALeRCE, Lasair) have proven the viability of real-time processing
- **LLM capabilities** have reached a point where agentic orchestration of scientific workflows is practical
- **Databricks/Spark ecosystem** provides the exact infrastructure needed for this scale of streaming data

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DATA SOURCES (Phase 1)                         │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │   ZTF    │  │   Fink   │  │ ANTARES  │  │  Rubin/LSST     │   │
│  │  Kafka   │  │   API    │  │   API    │  │  (early 2026)   │   │
│  │  Stream  │  │          │  │          │  │                  │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └───────┬──────────┘   │
│       │              │              │                │              │
└───────┼──────────────┼──────────────┼────────────────┼──────────────┘
        │              │              │                │
        ▼              ▼              ▼                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    INGESTION LAYER                                   │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              Databricks Structured Streaming                  │   │
│  │         (Spark Streaming + Kafka Consumer)                    │   │
│  └──────────────────────┬───────────────────────────────────────┘   │
│                         │                                           │
│  ┌──────────────────────▼───────────────────────────────────────┐   │
│  │                    Delta Lake                                 │   │
│  │  ┌─────────┐  ┌──────────┐  ┌──────────┐                    │   │
│  │  │ Bronze  │→ │  Silver  │→ │   Gold   │                    │   │
│  │  │ (raw)   │  │(cleaned) │  │(enriched)│                    │   │
│  │  └─────────┘  └──────────┘  └──────────┘                    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    AGENT LAYER                                       │
│                                                                     │
│  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────┐   │
│  │   Triage Agent  │  │ Cross-Reference  │  │  Anomaly Agent   │   │
│  │                 │  │     Agent        │  │                  │   │
│  │ • Classification│  │ • Gaia catalog   │  │ • Statistical    │   │
│  │ • Confidence    │  │ • SIMBAD lookup  │  │   outlier detect │   │
│  │ • Priority score│  │ • TNS matching   │  │ • Theory compare │   │
│  │                 │  │ • Literature     │  │ • Pattern finding│   │
│  └────────┬────────┘  └────────┬─────────┘  └────────┬─────────┘   │
│           │                    │                      │             │
│           └────────────────────┼──────────────────────┘             │
│                                │                                    │
│  ┌─────────────────────────────▼────────────────────────────────┐   │
│  │              Orchestrator Agent (LLM)                         │   │
│  │                                                               │   │
│  │  Routes alerts → appropriate specialist agents                │   │
│  │  Synthesizes multi-agent findings                             │   │
│  │  Decides escalation: routine / interesting / anomalous        │   │
│  │  Generates human-readable science summaries                   │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    OUTPUT LAYER                                      │
│                                                                     │
│  ┌────────────┐  ┌─────────────┐  ┌────────────┐  ┌────────────┐  │
│  │  Dashboard │  │  Alert Feed │  │  Reports   │  │  API       │  │
│  │  (Streamlit│  │  (Webhook/  │  │  (Nightly  │  │  (REST)    │  │
│  │   or Dash) │  │   Slack)    │  │   digest)  │  │            │  │
│  └────────────┘  └─────────────┘  └────────────┘  └────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Project Phases

### Phase 1: Foundation (Current)
- Ingest ZTF alert data via Fink REST API (immediate, no auth required)
- Build Delta Lake medallion architecture (bronze/silver/gold)
- Implement basic triage agent for transient classification
- Cross-reference with Gaia DR3 and SIMBAD
- Unit and integration test framework

### Phase 2: Real-Time Streaming
- Connect to Fink Kafka livestream (requires registration)
- Implement Databricks Structured Streaming pipeline
- Add ANTARES API integration
- Build anomaly detection agent with statistical outlier methods
- Nightly digest generation

### Phase 3: Agentic Intelligence
- LLM-orchestrated multi-agent pipeline
- Theory-aware validation (compare observations against predictions)
- Literature cross-referencing via ArXiv API
- Pattern discovery across alert history
- Confidence scoring and human-in-the-loop escalation

### Phase 4: Rubin/LSST Integration
- Adapt pipelines for Rubin alert schema
- Scale to ~10 million alerts/night
- Multi-messenger correlation (gravitational waves, neutrinos)
- Community contribution: publish filters, classifiers, anomaly reports

## Technology Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Streaming | Apache Kafka | Industry standard; ZTF/Fink native format |
| Processing | Apache Spark (Structured Streaming) | Scalable stream processing; Fink is built on Spark |
| Storage | Delta Lake (medallion architecture) | ACID transactions, time travel, schema enforcement |
| Catalog | Unity Catalog | Governance, lineage, access control |
| Compute | Databricks | Managed Spark, MLflow, collaborative notebooks |
| Agents | Python + Claude API / LangChain | LLM orchestration for scientific reasoning |
| Astronomy | astropy, astroquery, fink-client | Standard astronomy Python ecosystem |
| Serialization | Apache Avro | ZTF/Rubin native alert format |
| Dashboard | Streamlit / Plotly Dash | Rapid prototyping of science UI |
| Testing | pytest + Great Expectations | Code tests + data quality validation |
| CI/CD | GitHub Actions | Automated testing and deployment |

## Data Sources Reference

### ZTF (Zwicky Transient Facility)
- **Status**: Active, ~1M alerts/night
- **Access**: Kafka stream (auth required) or via community brokers
- **Format**: Apache Avro
- **Documentation**: https://www.ztf.caltech.edu/ztf-alert-stream.html

### Fink Broker
- **Status**: Active, processing full ZTF stream since 2020
- **Access**: REST API (public), Kafka livestream (registration required), Data Transfer service
- **Built on**: Apache Spark Structured Streaming
- **API**: https://api.fink-portal.org
- **Documentation**: https://fink-broker.readthedocs.io
- **Tutorials**: https://github.com/astrolabsoftware/fink-tutorials

### ANTARES Broker
- **Status**: Active, processing ZTF stream
- **Access**: Python client + API (public)
- **Client**: `pip install antares-client`
- **Documentation**: https://nsf-noirlab.gitlab.io/csdc/antares/client/

### Rubin/LSST
- **Status**: First light achieved June 2025; LSST survey begins early 2026
- **Alert stream**: Expected to begin January/February 2026
- **Volume**: ~10 million alerts/night (10x ZTF)
- **Alert production**: Will be continuous once begun
- **First data release (DR1)**: Expected by February 2028
- **Brokers**: Fink, ANTARES, ALeRCE, Lasair, Babamul, AMPEL, SNAPS all selected

### Cross-Reference Catalogs
- **Gaia DR3**: ~2 billion sources with precise astrometry, photometry, spectroscopy
- **SIMBAD**: Comprehensive astronomical database
- **TNS (Transient Name Server)**: Official IAU transient naming/reporting
- **NED**: NASA/IPAC Extragalactic Database
- **VizieR**: Astronomical catalog service

## Scientific Philosophy

### Dual Mandate

This project pursues two complementary scientific goals:

1. **Validation**: Observations that confirm existing theoretical predictions strengthen the frameworks being developed at the cutting edge. An automated system that efficiently validates known transient types frees human attention for the unknown.

2. **Discovery**: The most profound findings in physics often come from observations that break or challenge existing norms. Patterns in data that don't fit established models are not errors to be discarded — they are signals to be investigated. The anomaly detection pipeline is designed with this principle at its core.

### Rigor Requirements

- **No claim without statistical backing**: Every flagged anomaly must include confidence intervals, comparison baselines, and known-source exclusion
- **Reproducibility**: All analysis pipelines must be deterministic and version-controlled
- **Provenance**: Full data lineage from raw alert to final classification
- **Theory-aware**: Agents should know what the expected behavior is before flagging deviations
- **Human-in-the-loop**: Critical findings require human astronomer review before any public claim

## Getting Started

See [docs/SETUP.md](docs/SETUP.md) for detailed setup instructions.

### Quick Start (Local Development)
```bash
# Clone the repository
git clone https://github.com/<your-org>/agentic-galactic-discovery.git
cd agentic-galactic-discovery

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Fink API demo to verify connectivity
python src/ingestion/fink_api_demo.py

# Run tests
pytest tests/ -v
```

### Databricks Setup
```bash
# Install Databricks CLI
pip install databricks-cli

# Configure workspace connection
databricks configure --token

# Deploy notebooks
databricks workspace import_dir notebooks/ /Shared/agd/
```

## Project Structure

```
agentic-galactic-discovery/
│
├── README.md                          # This file
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # Apache 2.0
├── pyproject.toml                     # Python project configuration
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment variable template
│
├── docs/
│   ├── SETUP.md                       # Detailed setup guide
│   ├── ARCHITECTURE.md                # Detailed architecture documentation
│   ├── DATA_SOURCES.md                # Data source reference & schemas
│   ├── SCIENCE_GOALS.md               # Scientific objectives & methodology
│   └── AGENT_DESIGN.md                # Agent architecture & prompt design
│
├── src/
│   ├── __init__.py
│   │
│   ├── ingestion/                     # Data ingestion layer
│   │   ├── __init__.py
│   │   ├── fink_api_client.py         # Fink REST API client
│   │   ├── fink_stream_consumer.py    # Fink Kafka consumer
│   │   ├── antares_client.py          # ANTARES API client
│   │   ├── avro_deserializer.py       # ZTF Avro alert deserialization
│   │   └── schema_registry.py         # Alert schema management
│   │
│   ├── processing/                    # Data processing layer
│   │   ├── __init__.py
│   │   ├── bronze_processor.py        # Raw → Bronze (minimal transform)
│   │   ├── silver_processor.py        # Bronze → Silver (cleaned, validated)
│   │   ├── gold_processor.py          # Silver → Gold (enriched, aggregated)
│   │   ├── quality_checks.py          # Data quality validation
│   │   └── feature_engineering.py     # Derived features for ML/agents
│   │
│   ├── crossref/                      # Catalog cross-referencing
│   │   ├── __init__.py
│   │   ├── gaia_lookup.py             # Gaia DR3 cross-matching
│   │   ├── simbad_lookup.py           # SIMBAD object identification
│   │   ├── tns_lookup.py              # Transient Name Server matching
│   │   └── cone_search.py             # Generic cone search utility
│   │
│   ├── agents/                        # AI agent layer
│   │   ├── __init__.py
│   │   ├── orchestrator.py            # Master agent: routes & synthesizes
│   │   ├── triage_agent.py            # Initial classification & priority
│   │   ├── crossref_agent.py          # Multi-catalog cross-referencing
│   │   ├── anomaly_agent.py           # Statistical outlier detection
│   │   ├── theory_agent.py            # Compare against theoretical predictions
│   │   ├── prompts/                   # Agent prompt templates
│   │   │   ├── triage_system.md
│   │   │   ├── anomaly_system.md
│   │   │   └── orchestrator_system.md
│   │   └── tools/                     # Agent tool definitions
│   │       ├── catalog_tools.py
│   │       ├── analysis_tools.py
│   │       └── reporting_tools.py
│   │
│   ├── analysis/                      # Scientific analysis
│   │   ├── __init__.py
│   │   ├── light_curve.py             # Light curve analysis & fitting
│   │   ├── transient_classifier.py    # ML transient classification
│   │   ├── outlier_detection.py       # Statistical anomaly methods
│   │   └── periodicity.py             # Period finding for variable stars
│   │
│   ├── output/                        # Output & reporting layer
│   │   ├── __init__.py
│   │   ├── dashboard.py               # Streamlit dashboard
│   │   ├── nightly_digest.py          # Automated nightly summary
│   │   ├── alert_publisher.py         # Webhook/notification publisher
│   │   └── report_generator.py        # Science report generation
│   │
│   └── utils/                         # Shared utilities
│       ├── __init__.py
│       ├── config.py                  # Configuration management
│       ├── logging_config.py          # Structured logging
│       ├── coordinates.py             # Astronomical coordinate utilities
│       └── time_utils.py              # Julian date / MJD conversions
│
├── notebooks/                         # Databricks notebooks
│   ├── 01_fink_api_exploration.py     # Interactive Fink API exploration
│   ├── 02_bronze_ingestion.py         # Bronze layer streaming notebook
│   ├── 03_silver_processing.py        # Silver layer transforms
│   ├── 04_gold_enrichment.py          # Gold layer with cross-references
│   ├── 05_agent_prototype.py          # Agent experimentation
│   └── 06_anomaly_analysis.py         # Anomaly detection exploration
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                    # Shared fixtures
│   ├── test_ingestion/
│   │   ├── test_fink_api_client.py
│   │   ├── test_avro_deserializer.py
│   │   └── test_schema_registry.py
│   ├── test_processing/
│   │   ├── test_bronze_processor.py
│   │   ├── test_silver_processor.py
│   │   └── test_quality_checks.py
│   ├── test_crossref/
│   │   ├── test_gaia_lookup.py
│   │   └── test_simbad_lookup.py
│   ├── test_agents/
│   │   ├── test_triage_agent.py
│   │   └── test_orchestrator.py
│   └── test_analysis/
│       ├── test_light_curve.py
│       └── test_outlier_detection.py
│
├── data/
│   ├── sample_alerts/                 # Sample alert data for testing
│   ├── reference_catalogs/            # Local reference data subsets
│   └── test_fixtures/                 # Test data fixtures
│
├── config/
│   ├── default.yaml                   # Default configuration
│   ├── development.yaml               # Development overrides
│   ├── production.yaml                # Production configuration
│   └── alert_schemas/                 # Avro schema definitions
│       ├── ztf_alert.avsc
│       └── lsst_alert.avsc
│
└── scripts/
    ├── setup_databricks.sh            # Databricks workspace setup
    ├── download_sample_data.py        # Download sample alerts for development
    └── run_pipeline.sh                # Pipeline orchestration script
```

## License

Apache License 2.0 — See [LICENSE](LICENSE) for details.

## Acknowledgements

This project builds on the extraordinary work of:
- The **Zwicky Transient Facility** team and the ZTF Alert Distribution System
- The **Fink** broker collaboration (CNRS/IN2P3, IJCLab, Université Paris-Saclay)
- The **ANTARES** team (NSF NOIRLab, University of Arizona)
- The **Vera C. Rubin Observatory** / LSST project
- The **Gaia** mission (ESA)
- The global astronomical community that makes this data public

---

*"The most exciting phrase to hear in science, the one that heralds new discoveries, is not 'Eureka!' but 'That's funny...'"* — Isaac Asimov
