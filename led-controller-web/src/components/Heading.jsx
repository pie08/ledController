import { css, styled } from "styled-components";

const Heading = styled.h1`
  font-size: 3.6rem;
  line-height: 1.05;
  text-transform: uppercase;

  ${(props) =>
    props.as === "h2" &&
    css`
      font-size: 2.4rem;
    `}

  ${(props) =>
    props.as === "h3" &&
    css`
      font-size: 2rem;
    `}

  ${(props) =>
    props.$center &&
    css`
      text-align: center;
    `}
`;

export default Heading;
