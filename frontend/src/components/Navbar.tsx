import { useState } from "react";
import DashboardSVG from "../assets/dashboard.svg";
import ExclamtionSVG from "../assets/exclamation.svg";
import MyTaskSVG from "../assets/my-task.svg";
import TaskCategoriesSVG from "../assets/categories.svg";
import LogoutSVG from "../assets/logout.svg";
import NavButton from "./NavButton";

type currPage = "Dashboard" | "Vital Tasks" | "My Task" | "Task Categories"  

export default function Navbar(){
    
    const [ currPage, setcurrPage] = useState<currPage>("Dashboard")
    
    function handleClick(currPage: currPage){
        setcurrPage(currPage)
    }

    return(
        <div className="navbar flex flex-col rounded-[0_0.5rem_0.5rem_0] justify-between bg-pink text-white">
            <div className="links flex flex-col gap-6 items-center">
                <div className="header flex flex-col items-center">
                    <div className="rounded-full relative -top-8 w-19 h-19 bg-gray-200"></div>
                    <h3>Mothibi Malebana</h3>
                    <h4>mothibi.mm12@gmail.com</h4>
                </div>
                <NavButton title="Dashboard" linkTo="#" click={() => handleClick("Dashboard")} isActive={currPage == "Dashboard"} svg={DashboardSVG} />
                <NavButton title="Vital Task" linkTo="#" click={() => handleClick("Vital Tasks")} isActive={currPage == "Vital Tasks"} svg={ExclamtionSVG}/>
                <NavButton title="My Task" linkTo="#" click={() => handleClick("My Task")} isActive={currPage == "My Task"} svg={MyTaskSVG}/>
                <NavButton title="Task Categories" linkTo="#" click={() => handleClick("Task Categories")} isActive={currPage == "Task Categories"} svg={TaskCategoriesSVG}/>
            </div>
            <div className="footer flex flex-col items-center">
                <NavButton title="Logout" linkTo="login" svg={LogoutSVG}/>
            </div>
        </div>
    );
}