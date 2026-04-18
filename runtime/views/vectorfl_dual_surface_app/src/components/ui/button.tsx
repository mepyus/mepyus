import React from "react";
import { cx } from "@/lib/ui-utils";

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: "default" | "outline";
  size?: "default" | "sm";
};

export function Button({ className, variant = "default", size = "default", ...props }: ButtonProps) {
  const variants = {
    default: "border border-slate-900 bg-slate-900 text-white hover:bg-slate-800",
    outline: "border border-slate-300 bg-white text-slate-900 hover:bg-slate-50",
  };
  const sizes = {
    default: "h-10 px-4 py-2 text-sm",
    sm: "h-9 px-3 text-sm",
  };
  return (
    <button
      className={cx(
        "inline-flex items-center justify-center gap-2 rounded-xl font-semibold transition-colors disabled:pointer-events-none disabled:opacity-50",
        variants[variant],
        sizes[size],
        className,
      )}
      {...props}
    />
  );
}
