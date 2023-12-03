import { createContext, useContext, useState } from "react";

const PatternContext = createContext();

export function PatternProvider({ children }) {
  const [pattern, setPattern] = useState("rainbow");
  const [args, setArgs] = useState({});

  return (
    <PatternContext.Provider
      value={{
        pattern,
        setPattern,
        args,
        setArgs,
      }}
    >
      {children}
    </PatternContext.Provider>
  );
}

export function usePattern() {
  const context = useContext(PatternContext);
  if (context === undefined) {
    return new Error("PatternContext cannot be accessed outside of provider");
  }
  return context;
}
