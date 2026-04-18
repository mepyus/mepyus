import React from "react";

type MotionProps = React.HTMLAttributes<HTMLDivElement> & {
  initial?: unknown;
  animate?: unknown;
  transition?: unknown;
};

function MotionDiv({ initial: _initial, animate: _animate, transition: _transition, ...props }: MotionProps) {
  return <div {...props} />;
}

export const motion = {
  div: MotionDiv,
};
