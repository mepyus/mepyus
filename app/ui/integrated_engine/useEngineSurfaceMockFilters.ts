import { useMemo, useState } from "react";
import { AssetNode, AssetKind, AssetHealth } from "./engine-surface.types";

export function useEngineSurfaceMockFilters(assetTree: AssetNode[]) {
  const [search, setSearch] = useState("");
  const [kindFilter, setKindFilter] = useState<AssetKind | "all">("all");
  const [healthFilter, setHealthFilter] = useState<AssetHealth | "all">("all");
  const [sortBy, setSortBy] = useState<"default" | "attention" | "updated">("default");

  const filteredTree = useMemo(() => {
    const processNode = (node: AssetNode): AssetNode | null => {
      // 1. Kind & Health Filter (Leaf or Root)
      const matchesKind = kindFilter === "all" || node.kind === kindFilter;
      const matchesHealth = healthFilter === "all" || node.health === healthFilter;
      
      // 2. Search Text Match
      const matchesSearch = !search || 
        node.title.toLowerCase().includes(search.toLowerCase()) ||
        node.path.toLowerCase().includes(search.toLowerCase());

      // 3. Recursive process children
      const filteredChildren = node.children
        ?.map(processNode)
        .filter(Boolean) as AssetNode[];

      // Final match logic: Show if itself matches OR has matching children
      if ((matchesKind && matchesHealth && matchesSearch) || (filteredChildren && filteredChildren.length > 0)) {
        let result = { ...node, children: filteredChildren };
        return result;
      }
      return null;
    };

    let result = assetTree.map(processNode).filter(Boolean) as AssetNode[];

    // 4. Sorting (Flattened or Root Level)
    if (sortBy === "attention") {
      result.sort((a, b) => (b.attentionScore || 0) - (a.attentionScore || 0));
    } else if (sortBy === "updated") {
      result.sort((a, b) => b.updatedAt.localeCompare(a.updatedAt));
    }

    return result;
  }, [assetTree, search, kindFilter, healthFilter, sortBy]);

  return {
    search, setSearch,
    kindFilter, setKindFilter,
    healthFilter, setHealthFilter,
    sortBy, setSortBy,
    filteredTree
  };
}
