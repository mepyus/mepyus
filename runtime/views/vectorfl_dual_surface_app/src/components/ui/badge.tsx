import React from "react";
import { cx } from "@/lib/ui-utils";

type BadgeProps = React.HTMLAttributes<HTMLSpanElement> & {
  variant?: "default" | "outline";
};

export function Badge({ className, variant = "default", ...props }: BadgeProps) {
  const variants = {
    default: "border-transparent bg-white text-slate-950",
    outline: "border-zinc-700 bg-transparent text-zinc-300",
  };
  return (
    <span
      className={cx(
        "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors",
        variants[variant],
        className,
      )}
      {...props}
    />
  );
}
