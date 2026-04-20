from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(slots=True)
class WorkflowState:
    workflow_id: UUID
    vault_id: UUID
    state: str
    created_at: str


def create_trust_recompute_workflow(vault_id: UUID) -> WorkflowState:
    return WorkflowState(
        workflow_id=uuid4(),
        vault_id=vault_id,
        state="queued",
        created_at=datetime.now(timezone.utc).isoformat(),
    )
