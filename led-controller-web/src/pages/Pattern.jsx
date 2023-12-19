import styled from "styled-components";
import patterns from "../data/patterns.json";
import { useNavigate } from "react-router-dom";
import { usePattern } from "../context/PatternContext";
import Button from "../components/Button";

const PatternGrid = styled.div`
  display: grid;
  grid-template-columns: 1fr;
  gap: 2.4rem;
`;

const PatternBox = styled.button`
  width: 100%;
  padding: 6.4rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3.6rem;
  font-weight: 300;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--color-gray-50);
  background-image: url("/black-ab-bg.jpg");
  background-size: 150%;
  background-position: 10% 85%;
  transition: all 0.2s ease-in-out;

  &:hover {
    letter-spacing: 6px;
  }

  @media (max-width: 50em) {
    padding: 3.2rem;
    font-size: clamp(1rem, 4.5vw, 3rem);
  }
`;

const StyledButton = styled(Button)`
  position: fixed;
  bottom: 3.6rem;
  left: 50%;
  translate: -50% 0;
`;

function Patterns() {
  const navigate = useNavigate();
  const { setPattern } = usePattern();

  function handleClick(pattern) {
    setPattern(pattern);
    navigate("/");
  }

  return (
    <PatternGrid>
      {Object.keys(patterns).map((name) => (
        <PatternBox onClick={() => handleClick(name)} key={name}>
          {name}
        </PatternBox>
      ))}
      <StyledButton onClick={() => navigate(-1)}>Back</StyledButton>
    </PatternGrid>
  );
}

export default Patterns;
