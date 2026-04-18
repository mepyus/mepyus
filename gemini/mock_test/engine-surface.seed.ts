import { 
  AssetNode, 
  EngineEvent, 
  Recommendation, 
  Watchpoint, 
  BridgeItem,
  EngineIngestSlot,
  EnginePipelineSlot,
  ValidationReturnPacket
} from "./engine-surface.types";
import liveManifest from "./live_manifest.json";

// Dynamic Data Extraction from Central Manifest
export const assetTreeSeed: AssetNode[] = liveManifest.assets as AssetNode[];
export const engineEventsSeed: EngineEvent[] = liveManifest.events as EngineEvent[];
export const recommendationsSeed: Recommendation[] = liveManifest.recommendations as Recommendation[];
export const watchpointsSeed: Watchpoint[] = liveManifest.watchpoints as Watchpoint[];
export const bridgeItemsSeed: BridgeItem[] = liveManifest.bridgeItems as BridgeItem[];

// Slot Data (Newly Externalized)
export const ingestSlotSeed: EngineIngestSlot = liveManifest.ingestSlot as EngineIngestSlot;
export const pipelineSlotSeed: EnginePipelineSlot = liveManifest.pipelineSlot as EnginePipelineSlot;
export const validationReturnSlotSeed: ValidationReturnPacket = liveManifest.validationReturnSlot as ValidationReturnPacket;

// Engine Meta
export const engineStatusSeed = liveManifest.engine_status;
export const workMemorySeed = liveManifest.workMemory;
