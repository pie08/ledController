import styled, { css } from "styled-components";
import Heading from "../components/Heading";
import { usePattern } from "../context/PatternContext";
import Options from "../components/Options";
import patterns from "../data/patterns.json";
import { HiChevronDown } from "react-icons/hi2";
import { useState } from "react";

const Layout = styled.div`
  display: flex;
  flex-direction: column;
  gap: 2.4rem;
  width: 80%;
  margin: 0 auto;
  padding: 0 2.4rem;

  @media (max-width: 50em) {
    width: 100%;
    padding: 0;
  }
`;

const Header = styled.header`
  display: flex;
  justify-content: center;
`;

const PatternBox = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.8rem;
  position: relative;
`;

const Icon = styled(HiChevronDown)`
  font-size: 2.4rem;
  transition: all 0.2s;

  ${(props) =>
    props.$isOpen &&
    css`
      rotate: 180deg;
    `}
`;

const Divider = styled.div`
  display: block;
  height: 1px;
  background-color: var(--color-gray-50);
`;

const DropDownWrapper = styled.div`
  position: absolute;
  top: 100%;
  left: 0;
  pointer-events: none;
  padding-top: 1.2rem;
  z-index: 999;

  ${(props) =>
    props.$isOpen &&
    css`
      pointer-events: all;
    `}

  @media (max-width: 50em) {
    position: fixed;
    padding-top: 0;
    top: 2.4rem;
    left: 50%;
    translate: -50% 0;
    overflow-y: auto;
    height: 100%;
  }
`;

const DropDown = styled.ul`
  backdrop-filter: blur(2px);
  background-color: #404040bb;
  padding: 1.2rem;
  border-radius: 0.4rem;
  border: 1px solid var(--color-gray-600);
  list-style: none;
  font: inherit;

  opacity: 0;
  translate: 0 -1.2rem;
  transition: all 0.2s;

  ${(props) =>
    props.$isOpen &&
    css`
      opacity: 1;
      translate: 0 0;
    `}

  & li {
    cursor: pointer;
    padding: 0.6rem 0;
    transition: all 0.2s;

    &:hover {
      color: var(--color-gray-300);
    }

    &:not(:last-of-type) {
      border-bottom: 1px solid var(--color-gray-600);
    }
  }
`;

function Controller() {
  const { pattern, setPattern } = usePattern();
  const [isOpen, setIsOpen] = useState(false);

  return (
    <Layout>
      <Header>
        <PatternBox
          onMouseEnter={() => setIsOpen(true)}
          onMouseLeave={() => setIsOpen(false)}
        >
          <Heading>{pattern} </Heading>
          <Icon $isOpen={isOpen} />
          <DropDownWrapper $isOpen={isOpen}>
            <DropDown $isOpen={isOpen}>
              {Object.keys(patterns).map((name, i) => (
                <li
                  key={name}
                  onClick={() => {
                    setPattern(name);
                    setIsOpen(false);
                  }}
                >
                  {name}
                </li>
              ))}
            </DropDown>
          </DropDownWrapper>
        </PatternBox>
      </Header>
      <Divider />
      <Options options={patterns[pattern]} />
    </Layout>
  );
}

export default Controller;
