"""Shared test fixtures for the Agentic Galactic Discovery test suite."""

from __future__ import annotations

import pytest


@pytest.fixture
def sample_ztf_alert() -> dict:
    """A complete sample ZTF alert record as would be returned by Fink.

    This represents a single detection of a transient source, with
    the key fields used throughout the processing pipeline.
    """
    return {
        "objectId": "ZTF21aaxtctv",
        "candid": 1549473362115015004,
        "ra": 193.82238,
        "dec": 2.89612,
        "magpsf": 18.523,
        "sigmapsf": 0.048,
        "fid": 1,  # g-band
        "jd": 2459500.7234,
        "diffmaglim": 20.5,
        "rb": 0.95,  # real/bogus score (high = likely real)
        "drb": 0.98,  # deep learning real/bogus score
        "classtar": 0.01,  # star/galaxy classifier (low = galaxy-like)
        "distnr": 0.32,  # distance to nearest reference source (arcsec)
        "magnr": 19.8,  # magnitude of nearest reference source
        "v:classification": "SN candidate",
        "v:lastdate": "2024-01-15 08:33:05",
        "v:finkclass": "SN candidate",
    }


@pytest.fixture
def sample_alert_batch(sample_ztf_alert: dict) -> list[dict]:
    """A batch of sample alerts representing a light curve (multiple detections)."""
    alerts = []
    # Simulate a brightening transient over 5 detections
    mags = [19.5, 19.0, 18.5, 18.0, 17.8]
    jds = [2459495.5, 2459497.5, 2459500.5, 2459503.5, 2459506.5]
    fids = [1, 2, 1, 2, 1]  # alternating g and r bands

    for i, (mag, jd, fid) in enumerate(zip(mags, jds, fids)):
        alert = sample_ztf_alert.copy()
        alert["candid"] = 1549473362115015004 + i
        alert["magpsf"] = mag
        alert["jd"] = jd
        alert["fid"] = fid
        alerts.append(alert)

    return alerts


@pytest.fixture
def sample_fink_classes() -> list[str]:
    """List of all Fink classification labels."""
    return [
        "SN candidate",
        "Early SN Ia candidate",
        "SN Ia",
        "SN II",
        "Kilonova candidate",
        "Microlensing candidate",
        "AGN",
        "QSO",
        "Variable Star",
        "Cataclysmic Variable",
        "YSO",
        "Solar System MPC",
        "Solar System candidate",
        "Unknown",
    ]
