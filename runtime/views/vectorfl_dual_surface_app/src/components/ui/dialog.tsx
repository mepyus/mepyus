import React from "react";
import { cx } from "@/lib/ui-utils";

type DialogProps = {
  open: boolean;
  onOpenChange?: (open: boolean) => void;
  children: React.ReactNode;
};

export function Dialog({ open, children }: DialogProps) {
  if (!open) return null;
  return <div className="vui-dialog-root">{children}</div>;
}

export function DialogContent({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div className="vui-dialog-backdrop">
      <div className={cx("vui-dialog-content", className)} {...props} />
    </div>
  );
}

export function DialogHeader({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cx("vui-dialog-header", className)} {...props} />;
}

export function DialogFooter({ className, ...props }: React.HTMLAttributes<HTMLDivElement>) {
  return <div className={cx("vui-dialog-footer", className)} {...props} />;
}

export function DialogTitle({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) {
  return <h2 className={cx("vui-dialog-title", className)} {...props} />;
}

export function DialogDescription({ className, ...props }: React.HTMLAttributes<HTMLParagraphElement>) {
  return <p className={cx("vui-dialog-description", className)} {...props} />;
}
