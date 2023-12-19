import styled from "styled-components";
import Heading from "../components/Heading";
import { useNavigate } from "react-router-dom";
import { usePattern } from "../context/PatternContext";
import Options from "../components/Options";
import patterns from "../data/patterns.json";
import { HiArrowPath } from "react-icons/hi2";

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

const HeadingBox = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3.6rem;
`;

const Divider = styled.div`
  display: block;
  height: 1px;
  background-color: var(--color-gray-50);
`;

const ChangePatternButton = styled.button`
  line-height: 0;
  padding: 0.6rem;
  font-size: 2rem;
  color: var(--color-gray-50);
  transition: all 0.2s;

  &:hover {
    color: var(--color-gray-200);
  }
`;

function Controller() {
  const navigate = useNavigate();
  const { pattern } = usePattern();
  return (
    <Layout>
      <HeadingBox>
        <Heading>{pattern}</Heading>
        <ChangePatternButton onClick={() => navigate("/pattern")}>
          <HiArrowPath />
        </ChangePatternButton>
      </HeadingBox>
      <Divider />
      <Options options={patterns[pattern]} />
    </Layout>
  );
}

export default Controller;
