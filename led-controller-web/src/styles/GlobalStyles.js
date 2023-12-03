import { createGlobalStyle } from "styled-components";

const GlobalStyles = createGlobalStyle`
:root {
  /* --color-gray-950: #18212f;
  --color-gray-900: #111827;
  --color-gray-800: #1f2937;
  --color-gray-700: #374151;
  --color-gray-600: #4b5563;
  --color-gray-500: #6b7280;
  --color-gray-400: #9ca3af;
  --color-gray-300: #d1d5db;
  --color-gray-200: #e5e7eb;
  --color-gray-100: #f3f4f6;
  --color-gray-50: #f9fafb;
  --color-gray-0: #fff; */

  --color-gray-50: #FFFFFF;
  --color-gray-100: #F2F2F2;
  --color-gray-200: #D9D9D9;
  --color-gray-300: #BFBFBF;
  --color-gray-400: #A6A6A6;
  --color-gray-500: #8C8C8C;
  --color-gray-600: #737373;
  --color-gray-700: #595959;
  --color-gray-800: #404040;
  --color-gray-900: #262626;
  --color-gray-950: #1A1A1A;

  --color-yellow-700: #a16207;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 62.5%;
}

body {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 1.6rem;
  color: var(--color-gray-100);
  line-height: 1.5;
  min-height: 100vh;
  letter-spacing: 2px;
  padding: 3.2rem;
  background-color: var(--color-gray-900);
}

button {
  background: none;
  border: none;
  font-family: inherit;
  font-size: inherit;
  letter-spacing: inherit;
  color: inherit;
  cursor: pointer;
}
`;

export default GlobalStyles;
