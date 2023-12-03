import { BrowserRouter, Route, Routes } from "react-router-dom";
import GlobalStyles from "./styles/GlobalStyles";
import Patterns from "./pages/Pattern";
import Controller from "./pages/Controller";
import { PatternProvider } from "./context/PatternContext";

export default function App() {
  return (
    <PatternProvider>
      <BrowserRouter>
        <GlobalStyles />
        <Routes>
          <Route index path="/" element={<Controller />} />
          <Route path="/pattern" element={<Patterns />} />
          <Route path="*" element={<h1>Not found</h1>} />
        </Routes>
      </BrowserRouter>
    </PatternProvider>
  );
}
