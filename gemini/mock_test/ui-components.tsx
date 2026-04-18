import React, { createContext, useContext, useState } from "react";

export function cx(...args: any[]) { return args.filter(Boolean).join(" "); }

// --- Card ---
export function Card({ className, ...props }: any) { return <div className={cx("bg-zinc-900 border border-zinc-800 rounded-lg", className)} {...props} />; }
export function CardHeader({ className, ...props }: any) { return <div className={cx("p-4 border-b border-zinc-800", className)} {...props} />; }
export function CardTitle({ className, ...props }: any) { return <h3 className={cx("text-lg font-bold text-white", className)} {...props} />; }
export function CardDescription({ className, ...props }: any) { return <p className={cx("text-sm text-zinc-500", className)} {...props} />; }
export function CardContent({ className, ...props }: any) { return <div className={cx("p-4", className)} {...props} />; }

// --- Tabs ---
const TabsContext = createContext<any>(null);
export function Tabs({ defaultValue, value, onValueChange, className, children }: any) {
  const [val, setVal] = useState(defaultValue ?? value ?? "");
  return <TabsContext.Provider value={{ value: value ?? val, setValue: onValueChange ?? setVal }}>{children}</TabsContext.Provider>;
}
export function TabsList({ className, children }: any) { return <div className={cx("flex border-b border-zinc-800", className)}>{children}</div>; }
export function TabsTrigger({ value, className, children, ...props }: any) {
  const ctx = useContext(TabsContext);
  const active = ctx?.value === value;
  return <button className={cx("px-4 py-2 text-sm font-semibold border-b-2", active ? "border-blue-500 text-white" : "border-transparent text-zinc-500", className)} onClick={() => ctx?.setValue(value)} {...props}>{children}</button>;
}
export function TabsContent({ value, className, children }: any) {
  const ctx = useContext(TabsContext);
  return ctx?.value === value ? <div className={className}>{children}</div> : null;
}

// --- Others ---
export function Button({ className, variant, ...props }: any) { return <button className={cx("px-3 py-2 rounded-lg text-sm", className)} {...props} />; }
export function Badge({ className, variant, ...props }: any) { return <span className={cx("px-2 py-1 rounded-full text-[10px]", className)} {...props} />; }
export function Input({ className, ...props }: any) { return <input className={cx("p-2 rounded-lg bg-black/50 border border-zinc-800", className)} {...props} />; }
export function Textarea({ className, ...props }: any) { return <textarea className={cx("p-2 rounded-lg bg-black/50 border border-zinc-800", className)} {...props} />; }
export function Dialog({ children, open }: any) { return open ? <div className="fixed inset-0 bg-black/50 flex items-center justify-center">{children}</div> : null; }
export function DialogContent({ children }: any) { return <div className="bg-zinc-900 p-6 rounded-xl">{children}</div>; }
export function DialogHeader({ children }: any) { return <div className="mb-4">{children}</div>; }
export function DialogTitle({ children }: any) { return <h2 className="text-xl font-bold">{children}</h2>; }
export function DialogDescription({ children }: any) { return <p className="text-sm">{children}</p>; }
export function DialogFooter({ children }: any) { return <div className="flex justify-end gap-2">{children}</div>; }
