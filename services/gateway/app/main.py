from datetime import datetime, timezone
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Landmark Gateway", version="0.1.0")


class VaultIn(BaseModel):
    owner_name: str = Field(min_length=2)
    parcel_id: str


class VaultOut(VaultIn):
    id: UUID
    status: str = "pending_review"
    created_at: datetime


_VAULTS: dict[UUID, VaultOut] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "gateway",
        "version": app.version,
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/vaults", response_model=VaultOut, status_code=201)
def create_vault(payload: VaultIn) -> VaultOut:
    vault = VaultOut(id=uuid4(), created_at=datetime.now(timezone.utc), **payload.model_dump())
    _VAULTS[vault.id] = vault
    return vault


@app.get("/vaults/{vault_id}", response_model=VaultOut)
def get_vault(vault_id: UUID) -> VaultOut:
    vault = _VAULTS.get(vault_id)
    if not vault:
        raise HTTPException(status_code=404, detail="vault not found")
    return vault
