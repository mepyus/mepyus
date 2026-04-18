import { useMemo, useState } from "react";
import { AssetNode, EngineEvent, SummaryStats } from "./engine-surface.types";

export function useEngineSurfaceMockState(
  allAssets: AssetNode[], 
  allEvents: EngineEvent[]
) {
  const [selectedAssetId, setSelectedAssetId] = useState<string>("docs-guides");

  const selectedAsset = useMemo(
    () => allAssets.find((asset) => asset.id === selectedAssetId) ?? allAssets[0],
    [allAssets, selectedAssetId]
  );

  const selectedEvents = useMemo(
    () => allEvents.filter((event) => event.assetId === selectedAsset.id),
    [allEvents, selectedAsset]
  );

  const stats: SummaryStats = useMemo(() => {
    const watchCount = allAssets.filter((asset) => asset.health === "watch").length;
    const warningEvents = allEvents.filter((event) => event.type === "warning").length;
    const holds = allEvents.filter((event) => event.type === "hold").length;
    return {
      inventory: allAssets.length,
      watchCount,
      warningEvents,
      holds,
    };
  }, [allAssets, allEvents]);

  return {
    selectedAssetId,
    setSelectedAssetId,
    selectedAsset,
    selectedEvents,
    stats
  };
}
