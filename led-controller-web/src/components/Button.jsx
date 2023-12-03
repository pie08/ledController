import styled from "styled-components";

const Button = styled.button`
  background-color: var(--color-yellow-700);
  padding: 1.6rem 2.4rem;
  text-transform: uppercase;
  transition: all 0.2s;

  &:hover {
    letter-spacing: 4px;
  }
`;

export default Button;
