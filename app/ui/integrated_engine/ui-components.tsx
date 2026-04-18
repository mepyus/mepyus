import React, { createContext, useContext, useState } from "react";

export function cx(...args: any[]) { return args.filter(Boolean).join(" "); }

// --- Card (Refined to Surface Container) ---
export function Card({ className, ...props }: any) { return <div className={cx("bg-white border-none rounded-lg", className)} {...props} />; }
export function CardHeader({ className, ...props }: any) { return <div className={cx("p-4 border-b border-slate-100", className)} {...props} />; }
export function CardTitle({ className, ...props }: any) { return <h3 className={cx("text-lg font-semibold text-slate-900", className)} {...props} />; }
export function CardDescription({ className, ...props }: any) { return <p className={cx("text-sm text-slate-500", className)} {...props} />; }
export function CardContent({ className, ...props }: any) { return <div className={cx("p-4", className)} {...props} />; }

// --- Tabs (Refined to Flow State & Preserve State) ---
const TabsContext = createContext<any>(null);
export function Tabs({ defaultValue, value, onValueChange, className, children }: any) {
  const [val, setVal] = useState(defaultValue ?? value ?? "");
  return <TabsContext.Provider value={{ value: value ?? val, setValue: onValueChange ?? setVal }}>{children}</TabsContext.Provider>;
}
export function TabsList({ className, children }: any) { return <div className={cx("flex border-b border-slate-800 mb-0", className)}>{children}</div>; }
export function TabsTrigger({ value, className, children, ...props }: any) {
  const ctx = useContext(TabsContext);
  const active = ctx?.value === value;
  return <button className={cx("px-6 py-3 text-sm font-medium border-b-2 transition-colors", active ? "border-blue-500 text-blue-400" : "border-transparent text-slate-500 hover:text-slate-300", className)} onClick={() => ctx?.setValue(value)} {...props}>{children}</button>;
}
export function TabsContent({ value, className, children }: any) {
  const ctx = useContext(TabsContext);
  // unmount 대신 hidden 클래스를 사용하여 상태 유지
  return <div className={cx(ctx?.value === value ? "block" : "hidden", className)}>{children}</div>;
}

// --- Others (Refined Components) ---
export function Button({ className, variant, ...props }: any) { return <button className={cx("px-3 py-2 rounded-md text-sm font-medium transition-colors bg-slate-100 hover:bg-slate-200 text-slate-900", className)} {...props} />; }
export function Badge({ className, variant, ...props }: any) { return <span className={cx("px-2 py-0.5 rounded-full text-[10px] font-medium bg-slate-100 text-slate-600", className)} {...props} />; }
export function Input({ className, ...props }: any) { return <input className={cx("p-2 rounded-md bg-white border border-slate-200 focus:ring-1 focus:ring-blue-500 outline-none", className)} {...props} />; }
export function Textarea({ className, ...props }: any) { return <textarea className={cx("p-2 rounded-md bg-white border border-slate-200 focus:ring-1 focus:ring-blue-500 outline-none", className)} {...props} />; }
export function Dialog({ children, open }: any) { return open ? <div className="fixed inset-0 bg-slate-900/20 backdrop-blur-sm flex items-center justify-center">{children}</div> : null; }
export function DialogContent({ children }: any) { return <div className="bg-white p-6 rounded-xl shadow-lg border border-slate-100">{children}</div>; }
export function DialogHeader({ children }: any) { return <div className="mb-4">{children}</div>; }
export function DialogTitle({ children }: any) { return <h2 className="text-xl font-bold text-slate-900">{children}</h2>; }
export function DialogDescription({ children }: any) { return <p className="text-sm text-slate-500">{children}</p>; }
export function DialogFooter({ children }: any) { return <div className="flex justify-end gap-2">{children}</div>; }
