import { NavLink } from "react-router-dom";
import type { ButtonProps } from "./Button"
import { type MouseEventHandler } from "react";

interface NavButtonProps extends ButtonProps{
    isActive?: boolean
    click?: MouseEventHandler<HTMLButtonElement>
    linkTo: string
}

export default function NavButton({title, svg, isActive, click, linkTo}: NavButtonProps){
    return(
        <NavLink to={linkTo} end>
            <button onClick={click} className={`flex gap-4 w-72 h-16 py-5 pl-6 pr-4 rounded-xl hover:cursor-pointer ${isActive ? 'bg-white text-pink' : 'bg-pink text-white'}`}>
                <img src={svg} width="24" height="24" alt="button" />
                {title}
            </button>
        </NavLink>
    )
}