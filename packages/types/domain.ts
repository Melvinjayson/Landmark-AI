export type VaultStatus = "pending_review" | "active" | "restricted" | "archived";

export interface VaultSummary {
  id: string;
  ownerName: string;
  parcelId: string;
  status: VaultStatus;
  createdAt: string;
}

export interface TrustScore {
  vaultId: string;
  score: number;
  band: "low" | "medium" | "high";
  updatedAt: string;
}
