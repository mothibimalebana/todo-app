
export interface ButtonProps{
    title?: string;
    svg?: string;
}

export default function Button({title, svg,}: ButtonProps){

    return(
        <button className={`flex gap-4 w-72 h-16 py-5 pl-6 pr-4 rounded-xl hover:cursor-pointer`}>
            <img src={svg} width="24" height="24" alt="button" />
            {title}
        </button>
    );
}