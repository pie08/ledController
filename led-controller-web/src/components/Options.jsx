import styled, { css } from "styled-components";
import { usePattern } from "../context/PatternContext";
import { useForm } from "react-hook-form";
import Button from "./Button";
import hexRgb from "hex-rgb";
import { changeLed } from "../services/changeLed";
import { useState } from "react";
import { HiOutlinePlusCircle, HiOutlineXCircle } from "react-icons/hi2";

const Form = styled.form`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(30rem, 1fr));
  gap: 4.8rem 2.4rem;
  justify-items: center;
`;

const FormRow = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.6rem;
`;

const Label = styled.label`
  font-size: 1.6rem;
  font-weight: 500;
  text-transform: uppercase;
`;

const Input = styled.input`
  font: inherit;
  font-weight: 500;
  line-height: 0;
  font-size: 1.6rem;
  padding: 0.8rem 1.2rem;
  text-align: center;
  text-transform: uppercase;
  border: none;
  border-radius: 3px;

  ${(props) =>
    props.type === "checkbox" &&
    css`
      cursor: pointer;
      height: 2.4rem;
      width: 2.4rem;
    `}

  ${(props) =>
    props.$error &&
    css`
      outline: 3px solid #dc2626;
      background-color: #fee2e2;
      color: #dc2626;
    `}
`;

const ColorInput = styled.input.attrs({
  type: "color",
})`
  padding: 0;
  background-color: transparent;
  border: none;
  cursor: pointer;
  width: 4.8rem;
  height: 4.8rem;
`;

const AddColorButton = styled.button`
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  & svg {
    height: 2.4rem;
    width: 2.4rem;
    transition: all 0.3s;
  }

  &:hover svg {
    scale: 125%;
  }
`;

const ColorsContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.2rem;

  & button svg {
    height: 1.8rem;
    width: 1.8rem;
  }
`;

const SubmitButton = styled(Button)`
  position: fixed;
  bottom: 3.6rem;
  left: 50%;
  translate: -50% 0;
`;

function Options({ options: { args, defaultReset = false } }) {
  const { pattern } = usePattern();
  const { register, formState, handleSubmit } = useForm();
  const { errors } = formState;
  const [colors, setColors] = useState([]);

  function onSubmit(data) {
    if (data.color) {
      data.color = hexRgb(data.color, {
        format: "array",
      }).slice(0, -1);
    }

    if (data.colors) {
      data.colors = data.colors.map((color) =>
        hexRgb(color, {
          format: "array",
        }).slice(0, -1)
      );
    }

    if (colors.length) {
      data.colors = colors.map((color) =>
        hexRgb(color, {
          format: "array",
        }).slice(0, -1)
      );
    }

    console.log(data);
    changeLed({ pattern, args: data });
  }

  return (
    <Form onSubmit={handleSubmit(onSubmit)}>
      {args.map(({ optionName, defaultValue, type, inputType }) => (
        <FormRow key={optionName}>
          <Label htmlFor={optionName}>{optionName}</Label>

          {inputType === "input" && (
            <Input
              type={type}
              id={optionName}
              defaultValue={defaultValue}
              defaultChecked={type === "checkbox" && defaultValue}
              $error={errors[optionName]}
              {...register(optionName, {
                min: 0,
                max: 9999,
                valueAsNumber: true,
              })}
            />
          )}

          {inputType === "color" && (
            <ColorInput defaultValue="#990099" {...register(optionName)} />
          )}

          {inputType === "colors" && (
            <AddColorButton
              onClick={(e) => {
                e.preventDefault();
                setColors((state) => [...state, "#FFFFFF"]);
              }}
            >
              <HiOutlinePlusCircle />
            </AddColorButton>
          )}
        </FormRow>
      ))}

      <FormRow>
        <Label htmlFor="reset">Reset</Label>
        <Input
          type="checkbox"
          id="reset"
          defaultChecked={defaultReset}
          {...register("reset")}
        />
      </FormRow>

      {/* not controlled by react hook form */}
      {colors.map((color, i) => (
        <FormRow key={i}>
          <ColorsContainer>
            <button
              onClick={(e) => {
                e.preventDefault();
                setColors((state) =>
                  [...state].filter((_, index) => index !== i)
                );
              }}
            >
              <HiOutlineXCircle />
            </button>
            <ColorInput
              onChange={(e) => {
                setColors((colors) =>
                  colors.map((val, index) =>
                    index === i ? e.target.value : val
                  )
                );
              }}
              defaultValue={color}
            />
          </ColorsContainer>
        </FormRow>
      ))}

      <SubmitButton>send!</SubmitButton>
    </Form>
  );
}

export default Options;
