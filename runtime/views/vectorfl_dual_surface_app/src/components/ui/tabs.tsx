import React, { createContext, useContext, useState } from "react";
import { cx } from "@/lib/ui-utils";

type TabsContextValue = {
  value: string;
  setValue: (value: string) => void;
};

const TabsContext = createContext<TabsContextValue | null>(null);

export function Tabs({
  defaultValue,
  value,
  onValueChange,
  className,
  children,
}: React.HTMLAttributes<HTMLDivElement> & {
  defaultValue?: string;
  value?: string;
  onValueChange?: (value: string) => void;
}) {
  const [internalValue, setInternalValue] = useState(defaultValue ?? value ?? "");
  const activeValue = value ?? internalValue;
  const setValue = (nextValue: string) => {
    setInternalValue(nextValue);
    onValueChange?.(nextValue);
  };
  return (
    <TabsContext.Provider value={{ value: activeValue, setValue }}>
      <div className={cx("vui-tabs", className)}>{children}</div>
    </TabsContext.Provider>
  );
}

export function TabsList({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cx("grid gap-1", className)} {...props} />;
}

export function TabsTrigger({
  value,
  className,
  children,
}: React.ButtonHTMLAttributes<HTMLButtonElement> & { value: string }) {
  const context = useContext(TabsContext);
  const active = context?.value === value;
  return (
    <button
      type="button"
      className={cx("rounded-xl px-3 py-2 text-sm font-semibold text-zinc-400 transition-colors", className)}
      onClick={() => context?.setValue(value)}
      data-state={active ? "active" : "inactive"}
    >
      {children}
    </button>
  );
}

export function TabsContent({
  value,
  className,
  children,
}: React.HTMLAttributes<HTMLDivElement> & { value: string }) {
  const context = useContext(TabsContext);
  if (context?.value !== value) return null;
  return <div className={className}>{children}</div>;
}
