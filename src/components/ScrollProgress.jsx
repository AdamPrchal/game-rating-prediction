"use client";
import { useScrollPosition } from "../hooks/useScrollPosition";

export const ScrollProgress = () => {
  const scrollPosition = useScrollPosition();

  return (
    <progress
      value={scrollPosition}
      max="100"
      style={{ position: "sticky", top: 0 }}
    ></progress>
  );
};
