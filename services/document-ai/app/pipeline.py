from dataclasses import dataclass


@dataclass(slots=True)
class ExtractionResult:
    status: str
    confidence: float
    fields: dict[str, str]


def classify_result(confidence: float, fields: dict[str, str]) -> ExtractionResult:
    if confidence < 0.6:
        return ExtractionResult(status="needs_review", confidence=confidence, fields=fields)
    return ExtractionResult(status="complete", confidence=confidence, fields=fields)
