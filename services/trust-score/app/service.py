from dataclasses import dataclass


@dataclass(slots=True)
class TrustFactor:
    name: str
    impact: str
    weight: float


@dataclass(slots=True)
class TrustScoreResult:
    score: int
    band: str
    factors: list[TrustFactor]


def compute_trust_score(has_verified_identity: bool, doc_confidence: float, parcel_match: bool) -> TrustScoreResult:
    base = 50
    factors: list[TrustFactor] = []

    if has_verified_identity:
        base += 20
        factors.append(TrustFactor("identity_verified", "positive", 0.2))
    else:
        base -= 20
        factors.append(TrustFactor("identity_verified", "negative", 0.2))

    if doc_confidence >= 0.8:
        base += 20
        factors.append(TrustFactor("document_confidence", "positive", 0.2))
    elif doc_confidence >= 0.5:
        factors.append(TrustFactor("document_confidence", "neutral", 0.1))
    else:
        base -= 15
        factors.append(TrustFactor("document_confidence", "negative", 0.15))

    if parcel_match:
        base += 10
        factors.append(TrustFactor("parcel_match", "positive", 0.1))
    else:
        base -= 10
        factors.append(TrustFactor("parcel_match", "negative", 0.1))

    score = max(0, min(base, 100))
    if score >= 80:
        band = "high"
    elif score >= 50:
        band = "medium"
    else:
        band = "low"

    return TrustScoreResult(score=score, band=band, factors=factors)
